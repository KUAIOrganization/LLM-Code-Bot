#!/usr/bin/env python
# coding: utf-8


import json
import os

import glob
import numpy as np
import pandas as pd
import re

from .tokenizer import Tokenizers


class Dataset_Loaders:
    def __init__(self):
        base_log_dir = os.path.join("/workspace/logs", "run_" + datetime.datetime.now().strftime("%m_%d_%H_%M"))
        loader_log_dir = os.path.join(base_log_dir, "loader")
        self.tokenizer = Tokenizers()
        
    def load_CodeForces_A_difficulty(self):
        # Load problems
        with open(self.problems_path, 'r') as problems_file:
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
        raw_solutions = [[] for _ in range(515)] # 515 python submissions
        submissions = glob.glob(os.path.join(self.submissions_dir, "*.py"))

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
        
    def load_ProblemSolutionPythonV3(self):
        df = pd.read_csv(self.csv_path)

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
        problems, decoder_inputs, targets = tokenizer.tokenize(problems, solutions)
    
    def write_file(self, problems, decoder_inputs, targets, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, f"tokenized_padded_data.npz")
        np.savez_compressed(filepath, problems=problems, decoder_inputs=decoder_inputs, targets=targets)
        
def load_data(dataset_path):
    Loader = Dataset_Loaders()
    match dataset_path:
        case "/workspace/Training_Data/CodeForces_A_difficulty":
            Loader.load_CodeForces_A_difficulty()
            Loader.write_file("/workspace/Training_Data/CodeForces_A_difficulty")

        case "/workspace/Training_Data/ProblemSolutionV3":
            Loader.load_ProblemSolutionPythonV3()
            Loader.write_file("/workspace/Training_Data/ProblemSolutionV3")

        case "All":
            Loader.load_CodeForces_A_difficulty()
            Loader.load_ProblemSolutionPythonV3()
            Loader.write_file("/workspace/Training_Data/All")
        
        case _:
            "Invalid dataset"