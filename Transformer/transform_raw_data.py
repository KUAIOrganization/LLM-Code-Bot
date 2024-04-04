#!/usr/bin/env python
# coding: utf-8


import datetime
import json
import os

import glob
import numpy as np
import pandas as pd
import re

from .dataset import Dataset, Codeforces_A, Problem_Solution, All # Import all datasets
from .tokenizer import Tokenizers
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Dataset_Generator:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.loader_log_dir = os.path.join(self.base_dir, 'logs' + datetime.datetime.now().strftime('%m_%d_%H_%M'), 'loader')

        self.tokenizer = Tokenizers()
    
    def get_load_function(self, dataset):
        return getattr(self, 'load_' + dataset.name)

    def load_Codeforces_A(self):
        # Load problems
        problems_path = os.path.join(self.base_dir, Codeforces_A.raw_path, 'A_problems.json')
        with open(problems_path, 'r') as problems_file:
            problems_list = json.load(problems_file)

        raw_problems = {}
        for problem in problems_list:
            problem_id = problem['problem_id']
            concatenated_problem = 'XXSTATEMENT {} XXINPUT {} XXOUTPUT {} XXNOTES {} XXEXAMPLES {}'.format(
                problem.get('problem_statement', ''),
                problem.get('problem_input', ''),
                problem.get('problem_output', ''),
                problem.get('problem_notes', ''),
                problem.get('examples', '')
            )
            raw_problems[problem_id] = concatenated_problem

        # Load solutions
        submissions_dir = os.path.join(self.base_dir, Codeforces_A.raw_path, 'A_submissions')
        raw_solutions = [[] for _ in range(2000)] # Up to 2000 problem question indices | I would have this (2000) be a static variable at the top of the class -C.
        submissions = glob.glob(os.path.join(submissions_dir, '*.py'))

        for submission_path in submissions:
            problem_number = int(re.findall(r'^\d+', os.path.basename(submission_path))[0])
            with open(submission_path, 'r') as submission:
                raw_solutions[problem_number].append(submission.read())

        # Combine problems and solutions
        problems = []
        solutions = []
        for problem_id, solution_set in enumerate(raw_solutions):
            if solution_set:
                for solution in solution_set:
                    problems.append(raw_problems[problem_id])
                    solutions.append(solution)

        # Tokenize and pad
        encoder_inputs = self.tokenizer.tokenize_input(problems)
        decoder_inputs, targets = self.tokenizer.tokenize_output(solutions)
        
        try:
            assert all(len(encoder_inputs[0]) == len(seq) for seq in encoder_inputs), "Problems sequence lengths mismatch."
            assert all(len(decoder_inputs[0]) == len(seq) for seq in decoder_inputs), "Decoder inputs sequence lengths mismatch."
            assert all(len(targets[0]) == len(seq) for seq in targets), "Targets sequence lengths mismatch."
        except AssertionError as e:
            print(f"Discrepancy found in CodeForces_A sequence lengths: {e}")

        # Write to file
        Codeforces_A.write_tfrecord(encoder_inputs, decoder_inputs, targets, False)
        Codeforces_A.write_tfrecord(encoder_inputs, decoder_inputs, targets, True) # Reduced = True

    def load_Problem_Solution(self):
        problems_path = os.path.join(self.base_dir, Problem_Solution.raw_path, 'Problem_Solution.csv')
        df = pd.read_csv(problems_path, encoding_errors='ignore')

        problems = []
        solutions = []

        for index, row in df.iterrows():
            problem = row['Problem']
            solution = row['Python Code']
            problems.append(problem)
            solutions.append(solution)

        # Tokenize and pad
        encoder_inputs = self.tokenizer.tokenize_input(problems)
        decoder_inputs, targets = self.tokenizer.tokenize_output(solutions)

        try:
            assert all(len(encoder_inputs[0]) == len(seq) for seq in encoder_inputs), "Problems sequence lengths mismatch."
            assert all(len(decoder_inputs[0]) == len(seq) for seq in decoder_inputs), "Decoder inputs sequence lengths mismatch."
            assert all(len(targets[0]) == len(seq) for seq in targets), "Targets sequence lengths mismatch."
        except AssertionError as e:
            print(f"Discrepancy found in Problem_Solution sequence lengths: {e}")

        # Write to file
        Problem_Solution.write_tfrecord(encoder_inputs, decoder_inputs, targets, False)
        Problem_Solution.write_tfrecord(encoder_inputs, decoder_inputs, targets, True) # Reduced = True
    
    def load_All(self):
        # Generate datasets if they don't exist
        for dataset in Dataset.registry:
            if not os.path.exists(dataset.tokenized_path):
               load_function = self.get_load_function(dataset)
               load_function(dataset)
        
        # Pad to length of longest source
        cf_data = np.load(Codeforces_A.tokenized_path)
        cf_encoder_inputs = pad_sequences(cf_data['encoder_inputs'], padding='post', maxlen=Codeforces_A.max_length_input)
        cf_decoder_inputs = pad_sequences(cf_data['decoder_inputs'], padding='post', maxlen=Codeforces_A.max_length_output)
        cf_targets = pad_sequences(cf_data['targets'], padding='post', maxlen=Codeforces_A.max_length_output)

        ps_data = np.load(Problem_Solution.tokenized_path)
        ps_encoder_inputs = pad_sequences(ps_data['encoder_inputs'], padding='post', maxlen=Problem_Solution.max_length_input)
        ps_decoder_inputs = pad_sequences(ps_data['decoder_inputs'], padding='post', maxlen=Problem_Solution.max_length_output)
        ps_targets = pad_sequences(ps_data['targets'], padding='post', maxlen=Problem_Solution.max_length_output)

        # Concatenate the different data sources
        encoder_inputs = np.concatenate((cf_encoder_inputs, ps_encoder_inputs), axis=0)
        decoder_inputs = np.concatenate((cf_decoder_inputs, ps_decoder_inputs), axis=0)
        targets = np.concatenate((cf_targets, ps_targets), axis=0)
        
        # Write to file
        All.write_tfrecord(encoder_inputs, decoder_inputs, targets, False)
        All.write_tfrecord(encoder_inputs, decoder_inputs, targets, True) # Reduced = True