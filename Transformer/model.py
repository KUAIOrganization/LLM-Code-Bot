#!/usr/bin/env python
# coding: utf-8


from dataclasses import dataclass

import tensorflow as tf


@dataclass
class ModelArgs:
    dim: int = 512
    dim_ff = dim * 4
    num_layers: int = 6
    num_heads: int = 4
    dim_head: int = dim // num_heads

    problem_vocab_size: int = 0  # Set when the dataset is loaded
    solution_vocab_size: int = 0
    
    batch_size: int = 16
    learning_rate: float = 1e-4
    dropout_rate: float = 0.0 # Not used
    
    epochs: int = 2


def positional_encoder(seq_length, dim):
    # Generate positions
    positions = tf.range(seq_length, dtype=tf.float32)[..., tf.newaxis]
    
    # Compute division terms
    i = tf.range(dim, dtype=tf.float32)
    div_terms = 1 / tf.pow(10000.0, (2 * (i // 2)) / tf.cast(dim, tf.float32))
    
    # Calculate odd/even sinusoidal encodings
    angle_rates = positions * div_terms
    sine = tf.sin(angle_rates[:, 0::2])
    cosine = tf.cos(angle_rates[:, 1::2])
    
    # Interlace and reshape
    pos_encoding = tf.reshape(tf.concat([sine, cosine], axis=-1), [1, seq_length, dim])
    # print(tf.shape(pos_encoding))

    return pos_encoding


class EncoderLayer(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name='EncoderLayer'):
        super(EncoderLayer, self).__init__(name=name)

        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dim_key = args.dim_head
        self.num_heads = args.num_heads
        self.dropout_rate = args.dropout_rate

        # Self-Attention
        self.mha = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)

        # Feed-Forward
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name='encoder_ffn_dense1'), 
            tf.keras.layers.LeakyReLU(negative_slope=0.03), 
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name='encoder_ffn_dense2')
        ], name='encoder_ffn')

        # Normalization
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name='encoder_layernorm1')
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name='encoder_layernorm2')

        # Dropout
        self.dropout_mha = tf.keras.layers.Dropout(self.dropout_rate)
        self.dropout_ffn = tf.keras.layers.Dropout(self.dropout_rate)

    def call(self, x, training=False):
        # Self-Attention
        attn_output = self.mha(x, x)
        attn_output = self.dropout_mha(attn_output, training=training) # Dropout
        out1 = self.layernorm1(x + attn_output)  # Residual connection

        # Feed-Forward
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout_ffn(ffn_output, training=training) # Dropout
        out2 = self.layernorm2(out1 + ffn_output)  # Residual connection

        return out2

    def get_config(self):
        config = super(EncoderLayer, self).get_config()
        mha_config = self.mha.get_config()
        config.update({
            'dim': self.ffn.layers[2].units, 
            'dim_ff': self.ffn.layers[0].units, 
            'num_heads': mha_config['num_heads'], 
            'key_dim': mha_config['key_dim'], 
            'dropout_rate': self.dropout_mha.rate
        })
        return config


class DecoderLayer(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name='DecoderLayer'):
        super(DecoderLayer, self).__init__(name=name)
        
        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dropout_rate = args.dropout_rate
        self.num_heads = args.num_heads
        self.dim_key = args.dim_head # head = key

        # Self-Attention and Cross-Attention
        self.mha1 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)
        self.mha2 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)
        
        # Feed-Forward
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name='decoder_ffn_dense1'), 
            tf.keras.layers.LeakyReLU(negative_slope=0.03), 
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name='decoder_ffn_dense2')
        ], name='decoder_ffn')
        
        # Normalization
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name='decoder_layernorm1')
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name='decoder_layernorm2')
        self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name='decoder_layernorm3')
        
        # Dropout
        self.dropout_self_attn = tf.keras.layers.Dropout(self.dropout_rate)
        self.dropout_cross_attn = tf.keras.layers.Dropout(self.dropout_rate)
        self.dropout_ffn = tf.keras.layers.Dropout(self.dropout_rate)

    def call(self, x, enc_output, training=False, look_ahead_mask=None, padding_mask=None):
        # Self-Attention
        attn1_output = self.mha1(x, x, attention_mask=look_ahead_mask)
        attn1_output = self.dropout_self_attn(attn1_output, training=training) # Dropout
        out1 = self.layernorm1(x + attn1_output)  # Residual connection
        
        # Cross-Attention
        attn2_output = self.mha2(out1, enc_output, attention_mask=padding_mask)
        attn2_output = self.dropout_cross_attn(attn2_output, training=training) # Dropout
        out2 = self.layernorm2(out1 + attn2_output)  # Residual connection
        
        # Feed-Forward
        ffn_output = self.ffn(out2)
        ffn_output = self.dropout_ffn(ffn_output, training=training) # Dropout
        out3 = self.layernorm3(ffn_output + out2)  # Residual connection
        
        return out3

    def get_config(self):
        config = super(DecoderLayer, self).get_config()
        mha_config = self.mha1.get_config()  # Assumes mha1 and mha2 have the same configuration
        config.update({
            'dim': self.ffn.layers[2].units,
            'dim_ff': self.ffn.layers[0].units,
            'num_heads': mha_config['num_heads'],
            'key_dim': mha_config['key_dim'],
            'dropout_rate': self.dropout_self_attn.rate
        })
        return config


class TransformerEncoder(tf.keras.layers.Layer):
    def __init__(self, args, name='TransformerEncoder'):
        super(TransformerEncoder, self).__init__(name=name)
        self.num_layers = args.num_layers
        self.enc_layers = [EncoderLayer(args, name=f'encoder_layer_{i}') for i in range(self.num_layers)]

    def call(self, x: tf.Tensor, training=False) -> tf.Tensor:
        for layer in self.enc_layers:
            x = layer(x, training=training)
        return x


class TransformerDecoder(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name='TransformerDecoder'):
        super(TransformerDecoder, self).__init__(name=name)
        self.num_layers = args.num_layers
        self.dec_layers = [DecoderLayer(args, name=f'decoder_layer_{i}') for i in range(self.num_layers)]

    def call(self, x: tf.Tensor, enc_output: tf.Tensor, training=False) -> tf.Tensor:
        for layer in self.dec_layers:
            x = layer(x, enc_output, training=training)
        return x


class Transformer(tf.keras.Model):
    def __init__(self, args):
        super(Transformer, self).__init__()
        
        self.dim = args.dim
        self.problem_vocab_size = args.problem_vocab_size
        self.solution_vocab_size = args.solution_vocab_size

        # Separate embedding for input and output
        self.problem_embedding_layer = tf.keras.layers.Embedding(self.problem_vocab_size, self.dim, mask_zero=True)
        self.solution_embedding_layer = tf.keras.layers.Embedding(self.solution_vocab_size, self.dim, mask_zero=True)

        self.encoder = TransformerEncoder(args, name='encoder')
        self.decoder = TransformerDecoder(args, name='decoder')

        self.final_layer = tf.keras.layers.Dense(self.solution_vocab_size, name='output_layer')

    @tf.function
    def train_step(self, data):
        (encoder_input, decoder_input), target = data

        # Check for NaNs
        tf.debugging.check_numerics(encoder_input, "NaN in encoder_input")
        tf.debugging.check_numerics(decoder_input, "NaN in decoder_input")

        with tf.GradientTape() as tape:
            predictions = self((encoder_input, decoder_input[:, :-1]), training=True)
            
            # Mask PAD tokens
            mask = tf.cast(tf.math.logical_not(tf.math.equal(decoder_input[:, :-1], 0)), dtype=predictions.dtype)
            loss = self.compiled_loss(target, predictions, sample_weight=mask)

        # Compute and clip gradients
        gradients = tape.gradient(loss, self.trainable_variables)
        clipped_gradients, _ = tf.clip_by_global_norm(gradients, 10.0) # Hardcoded clip norm

        # Apply gradients to update model weights
        self.optimizer.apply_gradients(zip(clipped_gradients, self.trainable_variables))

        return loss

    def call(self, encoder_input, decoder_input, training=False):
        # print("Encoder input shape:", tf.shape(encoder_input))
        # print("Decoder input shape:", tf.shape(decoder_input))

        # Embeddings
        encoder_emb = self.problem_embedding_layer(encoder_input)
        decoder_emb = self.solution_embedding_layer(decoder_input)
        
        # Positional encodings
        input_seq_length = tf.shape(encoder_input)[1] # Old method works now
        output_seq_length = tf.shape(decoder_input)[1]
        encoder_emb += positional_encoder(input_seq_length, self.dim)
        decoder_emb += positional_encoder(output_seq_length, self.dim)
        # print("encoder_emb shape:", tf.shape(encoder_emb))
        # print("decoder_emb shape:", tf.shape(decoder_emb))
        
        # Forward pass
        encoder_output = self.encoder(encoder_emb, training=training)
        decoder_output = self.decoder(decoder_emb, encoder_output, training=training)

        final_output = self.final_layer(decoder_output)

        return final_output


def build_and_compile(args: ModelArgs):
    # Define model inputs
    encoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='encoder_input')
    decoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='decoder_input')

    # Initialize and call the Transformer
    transformer = Transformer(args)
    final_output = transformer(encoder_input, decoder_input)

    # Create the model
    model = tf.keras.Model(inputs=[encoder_input, decoder_input], outputs=final_output)

    # Compile the model
    # lr_schedule = tf.keras.optimizers.schedules.CosineDecay(initial_learning_rate=0.005, decay_steps=500, alpha=0.0001)
    # dataset size / batch size times epochs, is time until decay to alpha
    model.compile(
        optimizer = tf.keras.optimizers.Adam(learning_rate=args.learning_rate),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(ignore_class=0, from_logits=True),
        metrics=['accuracy'],
        run_eagerly=False
    )

    return model

# Not needed anymore
def calculate_loss(model_output, decoder_input, mask):
    loss = tf.keras.losses.sparse_categorical_crossentropy(decoder_input, model_output, from_logits=True)
    loss *= mask  # Apply mask
    return tf.reduce_sum(loss) / tf.reduce_sum(mask)