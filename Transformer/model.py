#!/usr/bin/env python
# coding: utf-8


import datetime
import os
from dataclasses import dataclass

import tensorflow as tf
import numpy as np

from .transform_raw_data import Dataset_Loader


@dataclass
class ModelArgs:
    dim: int = 256
    dim_ff = dim * 4
    num_layers: int = 6
    num_heads: int = 4
    dim_head = dim // num_heads
    
    problem_vocab_size: int = 0  # Set when the dataset is loaded
    solution_vocab_size: int = 0
    
    batch_size: int = 32
    learning_rate: float = 1e-4
    dropout_rate: float = 0.0
    
    epochs: int = 2


class Loader:
    def __init__(self, dataset_path, args: ModelArgs):
        self.batch_size = args.batch_size
        self.dataset_path = dataset_path
        self.dataset = None

    def create_dataset(self):
        # Ensure data exists
        if not os.path.exists(self.dataset_path):
            loader = Dataset_Loader(self.dataset_path)
            loader.load_data()
        
        # Load the .npz file
        data = np.load(self.dataset_path)
        problems = data['problems']
        decoder_inputs = data['decoder_inputs']
        targets = data['targets']
        
        # Create the dataset
        self.dataset = tf.data.Dataset.from_tensor_slices(((problems, decoder_inputs), targets))
        self.dataset.shuffle(buffer_size=1024).batch(self.batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)
        
        return self.dataset


def positional_encoder(seq_length, dim):
    # Generate positions for each element
    positions = tf.range(seq_length, dtype=tf.float32)[..., tf.newaxis]
    
    # Create a range for the dimensions and compute division terms
    i = tf.range(dim, dtype=tf.float32)
    div_terms = 1 / tf.pow(10000.0, (2 * (i // 2)) / tf.cast(dim, tf.float32))
    
    # Calculate odd/even sinusoidal encodings
    angle_rates = positions * div_terms
    sine = tf.sin(angle_rates[:, 0::2])
    cosine = tf.cos(angle_rates[:, 1::2])
    
    # Interlace and reshape
    pos_encoding = tf.reshape(tf.concat([sine, cosine], axis=-1), [1, seq_length, dim])
    
    return pos_encoding


class EncoderLayer(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name="EncoderLayer"):
        super(EncoderLayer, self).__init__(name=name)

        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dim_key = args.dim_head # dim_head
        self.num_heads = args.num_heads
        self.dropout_rate = args.dropout_rate

        # Multi-Head Self-Attention layer
        self.mha = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)

        # Feed-Forward Network Layers
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name="encoder_ffn_dense1"), 
            tf.keras.layers.LeakyReLU(alpha=0.01), # Trying LeakyReLu
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name="encoder_ffn_dense2")
        ], name="encoder_ffn")

        # Normalization Layers
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name="encoder_layernorm1")
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name="encoder_layernorm2")

        # Dropout
        self.dropout_mha = tf.keras.layers.Dropout(self.dropout_rate)
        self.dropout_ffn = tf.keras.layers.Dropout(self.dropout_rate)

    def call(self, x, training=False):
        # Self-Attention
        attn_output = self.mha(x, x)
        attn_output = self.dropout_mha(attn_output, training=training) # Dropout
        out1 = self.layernorm1(x + attn_output)  # Residual connection

        # Feed-Forward Network
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout_ffn(ffn_output, training=training) # Dropout
        out2 = self.layernorm2(out1 + ffn_output)  # Residual connection

        return out2

    def get_config(self):
        config = super(EncoderLayer, self).get_config()
        mha_config = self.mha.get_config()
        config.update({
            "dim": self.ffn.layers[2].units, 
            "dim_ff": self.ffn.layers[0].units, 
            "num_heads": mha_config['num_heads'], 
            "key_dim": mha_config['key_dim'], 
            "dropout_rate": self.dropout_mha.rate
        })
        return config


class DecoderLayer(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name="DecoderLayer"):
        super(DecoderLayer, self).__init__(name=name)
        
        self.dim = args.dim
        self.dim_ff = args.dim_ff
        self.dropout_rate = args.dropout_rate
        self.num_heads = args.num_heads
        self.dim_key = args.dim_head # dim_head

        # Self-Attention and Cross-Attention layers
        self.mha1 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)
        self.mha2 = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.dim_key)
        
        # Feed Forward Network Layers
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(self.dim_ff, kernel_initializer='he_normal', name="decoder_ffn_dense1"), 
            tf.keras.layers.LeakyReLU(alpha=0.01), # Trying LeakyReLu
            tf.keras.layers.Dense(self.dim, kernel_initializer='he_normal', name="decoder_ffn_dense2")
        ], name="decoder_ffn")
        
        # Normalization Layers
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name="decoder_layernorm1")
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name="decoder_layernorm2")
        self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6, name="decoder_layernorm3")
        
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
        
        # Feed-Forward Network
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
    def __init__(self, args, name="TransformerEncoder"):
        super(TransformerEncoder, self).__init__(name=name)
        self.num_layers = args.num_layers
        self.enc_layers = [EncoderLayer(args, name=f"encoder_layer_{i}") for i in range(self.num_layers)]

    def call(self, x: tf.Tensor, training=False) -> tf.Tensor:
        for layer in self.enc_layers:
            x = layer(x, training=training)
        return x


class TransformerDecoder(tf.keras.layers.Layer):
    def __init__(self, args: ModelArgs, name="TransformerDecoder"):
        super(TransformerDecoder, self).__init__(name=name)
        self.num_layers = args.num_layers
        self.dec_layers = [DecoderLayer(args, name=f"decoder_layer_{i}") for i in range(self.num_layers)]

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

        self.encoder = TransformerEncoder(args, name="encoder")
        self.decoder = TransformerDecoder(args, name="decoder")

        self.final_layer = tf.keras.layers.Dense(self.solution_vocab_size, name="output_layer")

    def call(self, encoder_input, decoder_input, training=False):
        # Embed input sequences
        encoder_emb = self.problem_embedding_layer(encoder_input)
        decoder_emb = self.solution_embedding_layer(decoder_input)
        
        # Generate and add positional encodings
        seq_length_enc = tf.shape(encoder_input)[1]
        seq_length_dec = tf.shape(decoder_input)[1]
        pos_encoding_enc = positional_encoder(seq_length_enc, self.dim)
        pos_encoding_dec = positional_encoder(seq_length_dec, self.dim)
        
        encoder_emb += pos_encoding_enc
        decoder_emb += pos_encoding_dec
        
        # Forward pass
        encoder_output = self.encoder(encoder_emb, training=training)
        decoder_output = self.decoder(decoder_emb, encoder_output, training=training)

        final_output = self.final_layer(decoder_output)

        return final_output


def build_and_compile():
    args = ModelArgs()

    # Define model inputs
    encoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='encoder_input')
    decoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='decoder_input')

    # Initialize and call the Transformer
    transformer = Transformer(args)
    final_output = transformer(encoder_input, decoder_input)

    # Create the model
    model = tf.keras.Model(inputs=[encoder_input, decoder_input], outputs=final_output)

    # Compile the model
    #lr_schedule = tf.keras.optimizers.schedules.CosineDecay(initial_learning_rate=0.005, decay_steps=500, alpha=0.0001)
    # dataset size / batch size times epochs, is time until decay to alpha
    model.compile(
        optimizer = tf.keras.optimizers.Adam(learning_rate=args.learning_rate),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(ignore_class=0, from_logits=True),
        metrics=['accuracy'],
        run_eagerly=False # !CAUTION!
    )

    return model


def calculate_loss(model_output, tokenized_code, mask):
    loss = tf.keras.losses.sparse_categorical_crossentropy(tokenized_code, model_output, from_logits=True)
    loss *= mask  # Apply mask
    return tf.reduce_sum(loss) / tf.reduce_sum(mask)

@tf.function
def train_step(model, optimizer, tokenized_question, tokenized_code, clip_norm=10.0):
    with tf.GradientTape() as tape:
        model_output = model([tokenized_question, tokenized_code], training=True)

        # Mask PAD tokens
        mask = tf.cast(tf.math.logical_not(tf.math.equal(tokenized_code, 0)), dtype=model_output.dtype)
        
        # Calculate loss
        average_loss = calculate_loss(model_output, tokenized_code, mask)

    # Compute and clip gradients
    gradients = tape.gradient(average_loss, model.trainable_variables)
    clipped_gradients, _ = tf.clip_by_global_norm(gradients, clip_norm)

    # Apply gradients to update model weights
    optimizer.apply_gradients(zip(clipped_gradients, model.trainable_variables))

    return average_loss


#print(len(loader.problem_tokenizer.word_index) + 1)
#print(len(loader.solution_tokenizer.word_index) + 1)

# Clears logs folder
#!find logs -mindepth 1 -delete

#tf.debugging.experimental.disable_dump_debug_info()

#!kill 415

#print("hello")

#print(tf.sysconfig.get_build_info())

#tf.__version__
#!tensorboard --version

#!pip install --upgrade tensorflow
#!pip install --upgrade tensorboard

#f.config.run_functions_eagerly(False)
#f.executing_eagerly()