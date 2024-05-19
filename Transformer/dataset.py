import numpy as np
import os
import tensorflow as tf


class Dataset:
    registry: list['Dataset'] = []

    def __init__(self, name):
        self.name = name
        self.raw_path = os.path.join('Training_Data', self.name)
        self.tokenized_path = os.path.join(self.raw_path, 'tokenized_padded_data.npz')

        Dataset.registry.append(self)

    def create_dataset(self, batch_size):
        # Load the .npz file
        data = np.load(self.tokenized_path)

        encoder_inputs = data['encoder_inputs']
        decoder_inputs = data['decoder_inputs']
        targets = data['targets']
        # print(np.shape(problems))
        # print(np.shape(decoder_inputs))
        # print(np.shape(targets))

        # Create the dataset
        dataset = tf.data.Dataset.from_tensor_slices(((encoder_inputs, decoder_inputs), targets))
        dataset = dataset.shuffle(buffer_size=1024).batch(batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)
        
    #     # Set cardinality for graph execution
    #     cardinality = self.get_cardinality(dataset)
    #     print(cardinality)
    #     print(cardinality == tf.data.experimental.INFINITE_CARDINALITY)
    #     print(cardinality == tf.data.experimental.UNKNOWN_CARDINALITY)

    #     self.count_batches(batch_size)
    #     print(self.num_batches)
    #     dataset = dataset.apply(tf.data.experimental.assert_cardinality(self.num_batches))
    #     cardinality = self.get_cardinality(dataset)
    #     print(cardinality)
    #     print(cardinality == tf.data.experimental.INFINITE_CARDINALITY)
    #     print(cardinality == tf.data.experimental.UNKNOWN_CARDINALITY)

        return dataset

    # def get_cardinality(self, dataset):
    #     #print(tf.data.experimental.cardinality(dataset).numpy())
    #     return tf.data.experimental.cardinality(dataset)
    
    # def count_batches(self, batch_size):
    #     data = np.load(self.tokenized_path)
    #     problems = data['problems']

    #     num_samples = problems.shape[0]
    #     self.num_batches = -(-num_samples // batch_size)
    
Codeforces_A = Dataset(
    'Codeforces_A'
)

Problem_Solution = Dataset(
    'Problem_Solution'
)

All = Dataset(
    'All'
)
