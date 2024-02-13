#!/usr/bin/env python
# coding: utf-8


import datetime
import json
import os

import glob
import numpy as np
import pandas as pd
import re

from .tokenizer import Tokenizers


class Dataset_Loader:
    def __init__(self, dataset_path):
        self.loader_log_dir = os.path.join("/workspace/logs" + datetime.datetime.now().strftime("%m_%d_%H_%M"), "loader")
        self.base_dir = "/workspace/Training_Data/"
        self.output_dir = dataset_path
        self.CodeForces_A_difficulty_dir = os.path.join(self.base_dir, "CodeForces_A_difficulty")
        self.ProblemSolutionPythonV3_dir = os.path.join(self.base_dir, "ProblemSolutionPythonV3")
        self.All_dir = os.path.join(self.base_dir, "All")

        self.tokenizer = Tokenizers()
        
    def load_CodeForces_A_difficulty(self):
        # Load problems
        problems_path = os.path.join(self.CodeForces_A_difficulty_dir, "A_problems.json")
        with open(problems_path, 'r') as problems_file:
            problems_list = json.load(problems_file)
        raw_problems = {}

        for problem in problems_list:
            problem_id = problem['problem_id']
            concatenated_problem = "XXSTATEMENT {} XXINPUT {} XXOUTPUT {} XXNOTES {} XXEXAMPLES {}".format(
                problem.get('problem_statement', ''),
                problem.get('problem_input', ''),
                problem.get('problem_output', ''),
                problem.get('problem_notes', ''),
                problem.get('examples', '')
            )
            raw_problems[problem_id] = concatenated_problem

        # Load solutions
        submissions_dir = os.path.join(self.CodeForces_A_difficulty_dir, "A_submissions")
        raw_solutions = [[] for _ in range(2000)] # Up to 2000 problem question indices
        submissions = glob.glob(os.path.join(submissions_dir, "*.py"))

        for submission_path in submissions:
            problem_number = int(re.findall(r'^\d+', os.path.basename(submission_path))[0])
            with open(submission_path, "r") as submission:
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
        problems = self.tokenizer.tokenize_input(problems)
        decoder_inputs, targets = self.tokenizer.tokenize_output(solutions)
        
        # Write data to a file
        self.write_file(problems, decoder_inputs, targets, self.CodeForces_A_difficulty_dir)

    def load_ProblemSolutionPythonV3(self):
        problems_path = os.path.join(self.ProblemSolutionPythonV3_dir, "ProblemSolutionPythonV3.csv")
        df = pd.read_csv(problems_path, encoding_errors='ignore')

        # Initialize problems and solutions lists
        problems = []
        solutions = []

        # Iterate over the DataFrame rows
        for index, row in df.iterrows():
            problem = row['Problem']
            solution = row['Python Code']
            problems.append(problem)
            solutions.append(solution)

        # Tokenize and pad
        problems = self.tokenizer.tokenize_input(problems)
        decoder_inputs, targets = self.tokenizer.tokenize_output(solutions)

        # Write data to a file
        self.write_file(problems, decoder_inputs, targets, self.ProblemSolutionPythonV3_dir)
    
    def load_All(self):
        # Load the npz files
        CodeForces_path = os.path.join(self.CodeForces_A_difficulty_dir, "tokenized_padded_data.npz")
        ProblemSolutionV3_path = os.path.join(self.ProblemSolutionPythonV3_dir, "tokenized_padded_data.npz")

        if not os.path.exists(CodeForces_path):
            temp_parent_dir = os.path.abspath(os.path.join(self.output_dir, os.pardir))
            self.output_dir = os.path.join(temp_parent_dir, "CodeForces_A_difficulty")
            self.load_CodeForces_A_difficulty()
        if not os.path.exists(ProblemSolutionV3_path):
            temp_parent_dir = os.path.abspath(os.path.join(self.output_dir, os.pardir))
            self.output_dir = os.path.join(temp_parent_dir, "ProblemSolutionPythonV3")
            self.load_ProblemSolutionPythonV3()
        
        cf_data = np.load(CodeForces_path)
        ps_data = np.load(ProblemSolutionV3_path)
        
        # Concatenate the files
        problems = np.concatenate((cf_data['problems'], ps_data['problems']), axis=0)
        decoder_inputs = np.concatenate((cf_data['decoder_inputs'], ps_data['decoder_inputs']), axis=0)
        targets = np.concatenate((cf_data['targets'], ps_data['targets']), axis=0)
        
        # Write data to a file
        self.write_file(problems, decoder_inputs, targets, self.All_dir)
    
    def write_file(self, problems, decoder_inputs, targets, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, f"tokenized_padded_data.npz")
        np.savez_compressed(filepath, problems=problems, decoder_inputs=decoder_inputs, targets=targets)
        
    def load_data(self):
        match self.output_dir:
            case "/workspace/Training_Data/CodeForces_A_difficulty/tokenized_padded_data.npz":
                self.load_CodeForces_A_difficulty()

            case "/workspace/Training_Data/ProblemSolutionV3/tokenized_padded_data.npz":
                self.load_ProblemSolutionPythonV3()

            case "/workspace/Training_Data/All/tokenized_padded_data.npz":
                self.load_All()

            case _:
                "Invalid dataset"