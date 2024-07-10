# workspace/Transformer/dataset.py

import numpy as np
import os
import tensorflow as tf


class Dataset:
    registry: list['Dataset'] = []

    def __init__(self, name):
        self.name = name
        self.base_path = os.path.join('Training_Data', self.name)
        self.raw_path = os.path.join(self.base_path, 'raw_data.npz')
        self.tokenized_path = os.path.join(self.base_path, 'tokenized_padded_data.npz')

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

        return dataset
    
Codeforces_A = Dataset('Codeforces_A')
LeetCode_Complete = Dataset('LeetCode_Complete')
LeetCode_Master = Dataset('LeetCode_Master')
LeetCode_Train = Dataset('LeetCode_Train')
Problem_Solution = Dataset('Problem_Solution')

All = Dataset('All')
