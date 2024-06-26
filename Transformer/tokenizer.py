#!/usr/bin/env python
# coding: utf-8


import io
import tokenize

import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Tokenizers:
    def __init__(self):
        self.problem_tokenizer = Tokenizer(filters='', oov_token='UNK')
        self.solution_tokenizer = Tokenizer(filters='', oov_token='UNK')
        # Also I would say to pass the SOS and EOS tokens as parameters. Probably have them have default values of 'XXSOS' and 'XXEOS' -C.
    
    def tokenize_input(self, problems):
        # Fit Keras tokenizer
        self.problem_tokenizer.fit_on_texts(problems)
        
        # Store tokenizer information
        with open('Transformer/model_files/problem_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.problem_tokenizer, f)
        
        # Tokenize with Keras tokenizer
        encoder_inputs = self.problem_tokenizer.texts_to_sequences(problems)
        
        # Pad to same length
        max_length_input = max(len(seq) for seq in encoder_inputs)
        encoder_inputs = pad_sequences(encoder_inputs, padding='post', maxlen=max_length_input)
        
        return encoder_inputs
    
    def tokenize_output(self, solutions):
        # Tokenize with Python tokenizer
        decoder_inputs = []
        targets = []
        for solution in solutions:
            tokens = []
            for token in tokenize.generate_tokens(io.StringIO(solution).readline): # generate_tokens only takes readlines
                tokens.append(token.string)
            decoder_inputs.append(['XXSOS'] + tokens)
            targets.append(tokens + ['XXEOS'])
        
        # Fit Keras tokenizer and tokenize
        self.solution_tokenizer.fit_on_texts(decoder_inputs + [['XXEOS']]) # Both at once
        decoder_inputs = self.solution_tokenizer.texts_to_sequences(decoder_inputs)
        targets = self.solution_tokenizer.texts_to_sequences(targets)

        # Pad to same length
        max_length_output = max(len(seq) for seq in targets)
        decoder_inputs = pad_sequences(decoder_inputs, padding='post', maxlen=max_length_output)
        targets = pad_sequences(targets, padding='post', maxlen=max_length_output)
        
        # Store tokenizer information
        with open('Transformer/model_files/solution_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.solution_tokenizer, f)

        return decoder_inputs, targets