#!/usr/bin/env python
# coding: utf-8


import pickle
import tokenize

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Tokenizers:
    def __init__(self, max_length_input, max_length_output):
        self.problem_tokenizer = Tokenizer(filters='', oov_token='UNK')
        self.max_length_input = 50
        self.max_length_output = 530
    
    def tokenize_input(self, problems):
        # Fit Keras tokenizer
        self.problem_tokenizer.fit_on_texts(problems)
        
        # Store tokenizer information
        with open('problem_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.problem_tokenizer, f)
        with open('solution_tokenizer.pkl', 'wb') as f:
            pickle.dump(self.solution_tokenizer, f)
        
        # Tokenize with Keras tokenizer
        problems = self.problem_tokenizer.texts_to_sequences(problems)
        
        # Pad to same length
        problems = pad_sequences(problems, padding='post', maxlen=self.max_length_input)
        
        return problems
    
    def tokenize_output(self, solutions):
        # Tokenize with Python tokenizer
        tokenized_solutions = []
        for solution in solutions:
            python_tokens = tokenize.generate_tokens(solution.readline).string
            tokenized_solutions.append(python_tokens)
        
        # Add SOS and EOS tokens
        decoder_inputs = [["XXSOS"] + s for s in tokenized_solutions]
        targets = [s + ["XXEOS"] for s in tokenized_solutions]
        
        # Pad to same length
        decoder_inputs = pad_sequences(decoder_inputs, padding='post', maxlen=self.max_length_output)
        targets = pad_sequences(targets, padding='post', maxlen=self.max_length_output)
        
        return decoder_inputs, targets