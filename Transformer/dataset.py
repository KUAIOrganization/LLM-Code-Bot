import numpy as np
import os
import tensorflow as tf


class Dataset:
    registry: list['Dataset'] = []

    def __init__(self, name, max_length_input, reduced_length_input, max_length_output, reduced_length_output):
        self.name = name
        self.raw_path = os.path.join('Training_Data', self.name)
        self.tokenized_path = os.path.join(self.raw_path, 'tokenized_padded_data.tfrecord')
        self.reduced_path = os.path.join(self.raw_path, 'tokenized_padded_reduced_data.tfrecord')

        self.max_length_input = max_length_input
        self.reduced_length_input = reduced_length_input

        self.max_length_output = max_length_output
        self.reduced_length_output = reduced_length_output
        
        Dataset.registry.append(self)
    
    def set_schema(self, reduced):
        self.schema = {
            'encoder_input': tf.io.FixedLenFeature([self.reduced_length_input if reduced else self.max_length_input], tf.int64),
            'decoder_input': tf.io.FixedLenFeature([self.reduced_length_output if reduced else self.max_length_output], tf.int64),
            'target': tf.io.FixedLenFeature([self.reduced_length_output if reduced else self.max_length_output], tf.int64),
        }

    def parse_tfrecord(self, example):
        # Parse single example
        return tf.io.parse_single_example(example, self.schema)

    def write_tfrecord(self, encoder_inputs, decoder_inputs, targets, reduced: bool):
        with tf.io.TFRecordWriter(self.reduced_path if reduced else self.tokenized_path) as writer:
            for encoder_input, decoder_input, target in zip(encoder_inputs, decoder_inputs, targets):
                # Skip sequences longer than the reduced limits
                if reduced and (encoder_input[self.reduced_length_input] or target[self.reduced_length_output]):
                    continue

                # Serialize the example
                example = tf.train.Example(features=tf.train.Features(feature={
                    'encoder_input': tf.train.Feature(int64_list=tf.train.Int64List(value=encoder_input)),
                    'decoder_input': tf.train.Feature(int64_list=tf.train.Int64List(value=decoder_input)),
                    'target': tf.train.Feature(int64_list=tf.train.Int64List(value=target)),
                }))
                writer.write(example.SerializeToString())

    def create_dataset(self, batch_size, reduced):
        self.set_schema(reduced) # Set schema

        # Load and parse tfrecord into encoder_inputs, decoder_inputs, targets
        raw_dataset = tf.data.TFRecordDataset(self.reduced_path if reduced else self.tokenized_path)
        parsed_dataset = raw_dataset.map(lambda x: self.parse_tfrecord(x)) # Calls self.parse_tfrecord()

        def map_to_model_inputs(parsed_example):
            # Maps to form ['encoder_input', 'decoder_input']
            return (({
                'encoder_input': parsed_example['encoder_input'],
                'decoder_input': parsed_example['decoder_input']
            }), parsed_example['target'])
    
        self.dataset = parsed_dataset.map(map_to_model_inputs)
        self.dataset.shuffle(buffer_size=1024).batch(batch_size).prefetch(tf.data.experimental.AUTOTUNE) # Buffer size?

        #return self.dataset

Codeforces_A = Dataset(
    'Codeforces_A',
    643, 530, 529, 200 # 180 reduced_length_output for all is good visual cutoff
)

Problem_Solution = Dataset(
    'Problem_Solution',
    98, 98, 1305, 200
)

All = Dataset(
    'All',
    max([dataset.max_length_input for dataset in Dataset.registry]), 
    max([dataset.reduced_length_input for dataset in Dataset.registry]),
    max([dataset.max_length_output for dataset in Dataset.registry]),
    max([dataset.reduced_length_output for dataset in Dataset.registry])
)
