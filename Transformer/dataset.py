import numpy
import os
import tensorflow as tf

from tensorflow.compat.v1.io import tf_record_iterator


class Dataset:
    registry: list['Dataset'] = []

    def __init__(self, name, input_length, output_length):
        self.name = name
        self.raw_path = os.path.join('Training_Data', self.name)
        self.tokenized_path = os.path.join(self.raw_path, 'tokenized_padded_data.tfrecord')

        self.input_length = input_length
        self.output_length = output_length
        
        self.num_batches = 0

        Dataset.registry.append(self)
    
    def set_schema(self):
        self.schema = {
            'encoder_input': tf.io.FixedLenFeature([self.input_length], tf.int64),
            'decoder_input': tf.io.FixedLenFeature([self.output_length], tf.int64),
            'target': tf.io.FixedLenFeature([self.output_length], tf.int64),
        }

    def parse_tfrecord(self, example):
        return tf.io.parse_single_example(example, self.schema)

    def write_tfrecord(self, encoder_inputs, decoder_inputs, targets):
        with tf.io.TFRecordWriter(self.tokenized_path) as writer:
            for encoder_input, decoder_input, target in zip(encoder_inputs, decoder_inputs, targets):
                # Serialize the example
                example = tf.train.Example(features=tf.train.Features(feature={
                    'encoder_input': tf.train.Feature(int64_list=tf.train.Int64List(value=encoder_input)),
                    'decoder_input': tf.train.Feature(int64_list=tf.train.Int64List(value=decoder_input)),
                    'target': tf.train.Feature(int64_list=tf.train.Int64List(value=target)),
                }))

                writer.write(example.SerializeToString())

    def create_dataset(self, batch_size):
        self.set_schema()
        self.count_batches(batch_size)

        # Load and parse tfrecord into encoder_inputs, decoder_inputs, targets
        raw_tfrecord = tf.data.TFRecordDataset(self.tokenized_path)
        parsed_dataset = raw_tfrecord.map(lambda x: self.parse_tfrecord(x))

        def map_to_model_inputs(parsed_example):
            # Maps to ['encoder_input', 'decoder_input']
            # To tuple or not to tuple...
            return ((
                parsed_example['encoder_input'],
                parsed_example['decoder_input']
            ), parsed_example['target'])
            return ({
                'encoder_input': parsed_example['encoder_input'],
                'decoder_input': parsed_example['decoder_input']
            }, parsed_example['target'])
    
        dataset = parsed_dataset.map(map_to_model_inputs, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        dataset = dataset.shuffle(buffer_size=1024)
        dataset = dataset.batch(batch_size)
        dataset = dataset.prefetch(tf.data.experimental.AUTOTUNE) # Buffer size?
        print("-------------------------------------------")
        print(self.num_batches)
        print("-------------------------------------------")
        dataset = dataset.apply(tf.data.experimental.assert_cardinality(self.num_batches)) # Set cardinality
        print("-------------------------------------------")
        cardinality = self.get_cardinality(dataset)
        print(cardinality)
        print(cardinality == tf.data.experimental.INFINITE_CARDINALITY)
        print(cardinality == tf.data.experimental.UNKNOWN_CARDINALITY)
        print("-------------------------------------------")
        self.dataset = dataset

        #self.num_batches = dataset.reduce(0, lambda x, _: x + 1).numpy()
        #print("---------------------------------")
        #print(self.num_batches)

        """
        self.num_batches = self.dataset.reduce(0, lambda x,_: x+1).numpy()
        print("---------------------------------")
        print(self.num_batches)"""

    @tf.function
    def get_cardinality(self, dataset):
        return tf.data.experimental.cardinality(dataset)
    
    def count_batches(self, batch_size):
        count = 0
        for _ in tf_record_iterator(self.tokenized_path):
            count += 1
        self.num_batches = -(-count // batch_size)

Codeforces_A = Dataset(
    'Codeforces_A',
    643, 529
)

Problem_Solution = Dataset(
    'Problem_Solution',
    98, 1305
)

All = Dataset(
    'All',
    max([dataset.input_length for dataset in Dataset.registry]), 
    max([dataset.output_length for dataset in Dataset.registry])
)
