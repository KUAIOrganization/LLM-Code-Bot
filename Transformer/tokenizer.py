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
        self.max_length_input = 50
        self.max_length_output = 530
    
    def tokenize_input(self, problems):
        # Fit Keras tokenizer
        self.problem_tokenizer.fit_on_texts(problems)
        
        # Store tokenizer information
        with open('Transformer/model_files/solution_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.problem_tokenizer, f)
        
        # Tokenize with Keras tokenizer
        problems = self.problem_tokenizer.texts_to_sequences(problems)
        
        # Pad to same length
        problems = pad_sequences(problems, padding='post', maxlen=self.max_length_input)
        
        return problems
    
    def tokenize_output(self, solutions):
        # Tokenize with Python tokenizer
        decoder_inputs = []
        targets = []
        for solution in solutions:
            tokens = []
            for token in tokenize.generate_tokens(io.StringIO(solution).readline): # generate_tokens only takes readlines
                tokens.append(token.string)
            decoder_inputs.append(["XXSOS"] + tokens)
            targets.append(tokens + ["XXEOS"])
        
        # Fit Keras tokenizer and tokenize
        self.solution_tokenizer.fit_on_texts(decoder_inputs + [["XXEOS"]]) # Both at once
        decoder_inputs = self.solution_tokenizer.texts_to_sequences(decoder_inputs)
        targets = self.solution_tokenizer.texts_to_sequences(targets)
        
        # Pad to same length
        decoder_inputs = pad_sequences(decoder_inputs, padding='post', maxlen=self.max_length_output)
        targets = pad_sequences(targets, padding='post', maxlen=self.max_length_output)

        # Store tokenizer information
        with open('Transformer/model_files/solution_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.solution_tokenizer, f)
        
        return decoder_inputs, targets