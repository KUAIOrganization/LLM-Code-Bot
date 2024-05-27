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
        self.generator_log_dir = os.path.join(self.base_dir, 'logs' + datetime.datetime.now().strftime('%m_%d_%H_%M'), 'generator')

        self.tokenizer = Tokenizers()
    
    def get_generate_function(self, dataset):
        return getattr(self, 'generate_' + dataset.name)

    def generate_Codeforces_A(self):
        # Load problems
        problems_path = os.path.join(self.base_dir, Codeforces_A.base_path, 'A_problems.json')
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
        submissions_dir = os.path.join(self.base_dir, Codeforces_A.base_path, 'A_submissions')
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

        # Write to npz
        self.write_file(problems, solutions, solutions, Codeforces_A.raw_path)
        self.write_file(encoder_inputs, decoder_inputs, targets, Codeforces_A.tokenized_path)

    def generate_Problem_Solution(self):
        problems_path = os.path.join(self.base_dir, Problem_Solution.base_path, 'Problem_Solution.csv')
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

        # Write to npz
        self.write_file(problems, solutions, solutions, Problem_Solution.raw_path)
        self.write_file(encoder_inputs, decoder_inputs, targets, Problem_Solution.tokenized_path)
    
    def generate_All(self):
        # Generate datasets
        for dataset in Dataset.registry:
            if dataset.name != "All" and not (os.path.exists(dataset.raw_path) and os.path.exists(dataset.tokenized_path)):
               generate_function = self.get_generate_function(dataset)
               generate_function()
        
        # Load datasets
        cf_data = np.load(Codeforces_A.raw_path)
        ps_data = np.load(Problem_Solution.raw_path)

        # Concatenate
        problems = np.concatenate((cf_data['encoder_inputs'], ps_data['encoder_inputs']), axis=0)
        solutions = np.concatenate((cf_data['decoder_inputs'], ps_data['decoder_inputs']), axis=0)
        
        # Tokenize and pad
        encoder_inputs = self.tokenizer.tokenize_input(problems)
        decoder_inputs, targets = self.tokenizer.tokenize_output(solutions)

        # Write to npz
        self.write_file(encoder_inputs, decoder_inputs, targets, All.tokenized_path)
    
    def write_file(self, encoder_inputs, decoder_inputs, targets, output_file):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        np.savez_compressed(output_file, encoder_inputs=encoder_inputs, decoder_inputs=decoder_inputs, targets=targets)

        # Convert to lists
        encoder_inputs_list = [seq.tolist() for seq in encoder_inputs]
        decoder_inputs_list = [seq.tolist() for seq in decoder_inputs]
        targets_list = [seq.tolist() for seq in targets]

        data = {
            'encoder_inputs': encoder_inputs_list,
            'decoder_inputs': decoder_inputs_list,
            'targets': targets_list
        }
        df = pd.DataFrame(data)
        excel_output_file = output_file.replace('.npz', '.xlsx')
        df.to_excel(excel_output_file, index=False)
