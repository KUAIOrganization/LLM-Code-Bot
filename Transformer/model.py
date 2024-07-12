# workspace/Transformer/model.py

from dataclasses import dataclass
import tensorflow as tf


@dataclass
class ModelArgs:
    dim: int = 256
    dim_ff: int = dim * 4
    num_layers: int = 4
    num_heads: int = 2
    dim_head: int = dim // num_heads

    problem_vocab_size: int = 0  # Set when the dataset is loaded
    solution_vocab_size: int = 0
    
    batch_size: int = 32
    dropout_rate: float = 0.1
    learning_rate: float = 1e-4 # Not used with Noam
    clip_norm: float = 10.0
    
    epochs: int = 100

    def get_config(self):
        return {
            'dim': self.dim,
            'dim_ff': self.dim_ff,
            'num_layers': self.num_layers,
            'num_heads': self.num_heads,
            'dim_head': self.dim_head,
            'problem_vocab_size': self.problem_vocab_size,
            'solution_vocab_size': self.solution_vocab_size,
            'batch_size': self.batch_size,
            'learning_rate': self.learning_rate,
            'dropout_rate': self.dropout_rate,
            'epochs': self.epochs
        }

    @classmethod
    def from_config(cls, config):
        return cls(**config)

class NoamSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, dim, warmup_steps=4_000):
        super(NoamSchedule, self).__init__()
        self.dim = tf.cast(dim, tf.float32)
        self.warmup_steps = warmup_steps
    
    def __call__(self, step):
        step = tf.cast(step, tf.float32)
        arg1 = tf.math.rsqrt(step)
        arg2 = step * (self.warmup_steps ** -1.5)
        return tf.math.rsqrt(self.dim) * tf.math.minimum(arg1, arg2)
    
    def get_config(self):
        return {
            'dim': self.dim.numpy(), 
            'warmup_steps': self.warmup_steps
        }
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)

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
    def __init__(self, args: ModelArgs, layer_index: int, name='EncoderLayer', **kwargs):
        super(EncoderLayer, self).__init__(name=name, **kwargs)
        self.layer_index = layer_index
        self.args = args

        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dropout_rate = args.dropout_rate
        self.num_heads = args.num_heads
        self.dim_key = args.dim_head

    def build(self, input_shape):
        prefix = f'encoder{self.layer_index}'

        # Self-Attention
        self.mha = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key, name=f'{prefix}_mha')

        # Feed-Forward
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name=f'{prefix}_ffn_dense1'), 
            tf.keras.layers.LeakyReLU(negative_slope=0.03), 
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name=f'{prefix}_ffn_dense2')
        ], name=f'{prefix}_ffn')

        # Normalization
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name=f'{prefix}_layernorm1')
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name=f'{prefix}_layernorm2')

        # Dropout
        self.dropout_mha = tf.keras.layers.Dropout(self.dropout_rate, name=f'{prefix}_dropout_mha')
        self.dropout_ffn = tf.keras.layers.Dropout(self.dropout_rate, name=f'{prefix}_dropout_ffn')

        self.layers = [
            self.mha, self.ffn, 
            self.layernorm1, self.layernorm2, 
            self.dropout_mha, self.dropout_ffn
        ]
        super(EncoderLayer, self).build(input_shape)

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
        config.update({'layer_index': self.layer_index, 'args': self.args})
        return config

    @classmethod
    def from_config(cls, config):
        layer_index = config.pop('layer_index')
        args = config.pop('args')
        return cls(layer_index=layer_index, args=args, **config)


class DecoderLayer(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, layer_index: int, name='DecoderLayer', **kwargs):
        super(DecoderLayer, self).__init__(name=name, **kwargs)
        self.layer_index = layer_index
        self.args = args
        
        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dropout_rate = args.dropout_rate
        self.num_heads = args.num_heads
        self.dim_key = args.dim_head

    def build(self, input_shape):
        prefix = f'decoder{self.layer_index}'

        # Self-Attention and Cross-Attention
        self.mha1 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key, name=f'{prefix}_mha1')
        self.mha2 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key, name=f'{prefix}_mha2')
        
        # Feed-Forward
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name=f'{prefix}_ffn_dense1'), 
            tf.keras.layers.LeakyReLU(negative_slope=0.03), 
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name=f'{prefix}_ffn_dense2')
        ], name='decoder_ffn')
        
        # Normalization
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name=f'{prefix}_layernorm1')
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name=f'{prefix}_layernorm2')
        self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name=f'{prefix}_layernorm3')
        
        # Dropout
        self.dropout_self_attn = tf.keras.layers.Dropout(self.dropout_rate, name=f'{prefix}_dropout_self_attn')
        self.dropout_cross_attn = tf.keras.layers.Dropout(self.dropout_rate, name=f'{prefix}_dropout_cross_attn')
        self.dropout_ffn = tf.keras.layers.Dropout(self.dropout_rate, name=f'{prefix}_dropout_ffn')

        self.layers = [
            self.mha1, self.mha2, self.ffn, 
            self.layernorm1, self.layernorm2, self.layernorm3, 
            self.dropout_self_attn, self.dropout_cross_attn, self.dropout_ffn
        ]
        super(DecoderLayer, self).build(input_shape)

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
        config.update({'layer_index': self.layer_index, 'args': self.args})
        return config
    
    @classmethod
    def from_config(cls, config):
        layer_index = config.pop('layer_index')
        args = config.pop('args')
        return cls(layer_index=layer_index, args=args, **config)


class TransformerEncoder(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name='Encoder'):
        super(TransformerEncoder, self).__init__(name=name)
        self.args = args
        self.num_layers = args.num_layers
        self.layers = [EncoderLayer(args, layer_index=i, name=f'encoder_layer_{i}') for i in range(self.num_layers)]

    def build(self, input_shape):
        for layer in self.layers:
            layer.build(input_shape)
        super(TransformerEncoder, self).build(input_shape)

    def call(self, x: tf.Tensor, training=False) -> tf.Tensor:
        for layer in self.layers:
            x = layer(x, training=training)
        return x
    
    def get_config(self):
        config = super(Transformer, self).get_config()
        config.update({'layer_index': self.layer_index, 'args': self.args})
        return config

    @classmethod
    def from_config(cls, config):
        layer_index = config.pop('layer_index')
        args = config.pop('args')
        return cls(layer_index=layer_index, args=args)


class TransformerDecoder(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name='Decoder'):
        super(TransformerDecoder, self).__init__(name=name)
        self.args = args
        self.num_layers = args.num_layers
        self.layers = [DecoderLayer(args, layer_index=i, name=f'decoder_layer_{i}') for i in range(self.num_layers)]

    def build(self, input_shape):
        for layer in self.layers:
            layer.build(input_shape)
        super(TransformerDecoder, self).build(input_shape)

    def call(self, x: tf.Tensor, enc_output: tf.Tensor, training=False) -> tf.Tensor:
        for layer in self.layers:
            x = layer(x, enc_output, training=training)
        return x

    def get_config(self):
        config = super(TransformerDecoder, self).get_config()
        config.update({'args': self.args})
        return config
    
    @classmethod
    def from_config(cls, config):
        args = config.pop('args')
        return cls(args=args, **config)


class Transformer(tf.keras.Model):
    def __init__(self, args: ModelArgs):
        super(Transformer, self).__init__()
        self.args = args
        
        self.dim = args.dim
        self.problem_vocab_size = args.problem_vocab_size
        self.solution_vocab_size = args.solution_vocab_size

        # Separate embedding for input and output
        self.problem_embedding = tf.keras.layers.Embedding(
            self.problem_vocab_size, self.dim, mask_zero=True, name="problem_embedding")
        self.solution_embedding = tf.keras.layers.Embedding(
            self.solution_vocab_size, self.dim, mask_zero=True, name="solution_embedding")

        # Transformer blocks
        self.encoder = TransformerEncoder(args, name='Encoder')
        self.decoder = TransformerDecoder(args, name='Decoder')

        # Output
        self.final_layer = tf.keras.layers.Dense(self.solution_vocab_size, name='output_layer')

    def build(self, input_shape):
        self.problem_embedding.build(input_shape[0])
        self.solution_embedding.build(input_shape[1])
        self.encoder.build(input_shape[0])
        self.decoder.build(input_shape[1])
        self.final_layer.build((input_shape[1][0], input_shape[1][1], self.dim))
        super(Transformer, self).build(input_shape)

    @tf.function
    def train_step(self, data):
        (encoder_input, decoder_input), target = data

        with tf.GradientTape() as tape:
            predictions = self((encoder_input, decoder_input[:, :-1]), training=True)
            
            mask = tf.cast(tf.math.logical_not(tf.math.equal(decoder_input[:, :-1], 0)), dtype=predictions.dtype)
            loss = self.compiled_loss(target, predictions, sample_weight=mask)

        # Gradients
        gradients = tape.gradient(loss, self.trainable_variables)
        clipped_gradients, _ = tf.clip_by_global_norm(gradients, self.args.clip_norm)

        self.optimizer.apply_gradients(zip(clipped_gradients, self.trainable_variables))

        return loss

    def call(self, encoder_input, decoder_input, training=False):
        # Embeddings
        encoder_emb = self.problem_embedding(encoder_input)
        decoder_emb = self.solution_embedding(decoder_input)
        
        # Positional encodings
        input_seq_length = tf.shape(encoder_input)[1]
        output_seq_length = tf.shape(decoder_input)[1]
        encoder_emb += positional_encoder(input_seq_length, self.dim)
        decoder_emb += positional_encoder(output_seq_length, self.dim)
        
        # Forward pass
        encoder_output = self.encoder(encoder_emb, training=training)
        decoder_output = self.decoder(decoder_emb, encoder_output, training=training)

        final_output = self.final_layer(decoder_output)

        return final_output
    
    def get_config(self):
        config = super(Transformer, self).get_config()
        config.update({'args': self.args.get_config()})
        return config

    @classmethod
    def from_config(cls, config):
        args = ModelArgs.from_config(config.pop('args'))
        return cls(args=args)
    
    def build_from_config(self, config):
        self.build(config['input_shape'])


def build_and_compile(args: ModelArgs):
    # Inputs
    encoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='encoder_input')
    decoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='decoder_input')

    # Transformer
    transformer = Transformer(args)
    transformer.build([(None, None), (None, None)]) # batch_size, len(encoder_input), batch_size, len(decoder_input)
    final_output = transformer(encoder_input, decoder_input)

    # Model
    model = tf.keras.Model(inputs=[encoder_input, decoder_input], outputs=final_output, name="Code_SLM")
    model.compile(
        optimizer = tf.keras.optimizers.Adam(learning_rate=NoamSchedule(args.dim)),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(ignore_class=0, from_logits=True),
        metrics=['accuracy'],
        run_eagerly=False
    )

    return model