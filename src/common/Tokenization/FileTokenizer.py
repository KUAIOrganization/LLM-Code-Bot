import tensorflow
Keras = tensorflow.keras

import numpy as Numpy
import re
import json
import glob
import os

TOKEN_FOLDER_LOCATION = "C:\AIClub\Code\Large Dataset\Tokenized"
TOKEN_FILE_LOCATION = TOKEN_FOLDER_LOCATION + "\\tokens.json"
TOKENIZED_PROBLEMS_LOCATION = TOKEN_FOLDER_LOCATION + "\\problem_tokenized_"
TOKENIZED_SUBMISSIONS_LOCATION = TOKEN_FOLDER_LOCATION + "\\submission_tokenized_"
SEQUENCE_LENGTH = 530

class Load:
    def __init__(self, problems_path, submissions_dir):
        self.problems_path = problems_path
        self.submissions_dir = submissions_dir
        self.problems = {}
        self.solutions = []
        self.tokenizer = Keras.layers.TextVectorization(standardize="lower", split="whitespace", ngrams=10, max_tokens=400)
        print(self.tokenizer.get_config())
        self.problem_padded = None
        self.solution_padded = None
        self.dataset = None

    def load_problems(self):
        # Load problem descriptions
        with open(self.problems_path, 'r') as f:
            problems_list = json.load(f)

        # Populate self.problems as a dictionary
        for problem in problems_list:
            id = problem['problem_id'] # Unused
            statement = problem.get('problem_statement', '')
            input = problem.get('problem_input', '')
            output = problem.get('problem_output', '')
            notes = problem.get('problem_notes', '')
            examples = problem.get('examples', '')

            # Concatenate attributes using hyperidentifiers
            concatenated_problem = f"XXSTATEMENT {statement} XXINPUT {input} XXOUTPUT {output} XXNOTES {notes} XXEXAMPLES {examples}"
            self.problems[id] = concatenated_problem

    def load_solutions(self):
        # Load code solutions into self.solutions list
        for filepath in glob.glob(f"{self.submissions_dir}/*.py"):
            filename = os.path.basename(filepath)
            print("filename: ", filename)

            # Extract the problem number of the submission
            problem_number = int(re.findall(r'^\d+', filename)[0])
            # Extract the matching problem
            problem_content = self.problems.get(int(problem_number), None)
            if problem_content is None:
                print(problem_number)

            with open(filepath, "r") as f:
                self.solutions.append((problem_number, f.read()))

    def tokenize_and_pad(self):
        self.tokenizer.compile()
        self.tokenizer.adapt(list(self.problems.values()) + [solution for _, solution in self.solutions])

        # Searches for matching problems for each solution
        problem_sequences = []
        solution_sequences = []
        for problem_number, solution in self.solutions:
            print(problem_number)
            problem_content = self.problems.get(problem_number, None)
            problem_sequence = self.tokenizer.call([problem_content])[0]
            solution_sequence = self.tokenizer.call([solution])[0]
            problem_sequences.append(problem_sequence)
            solution_sequences.append(solution_sequence)

        self.problem_padded = Keras.preprocessing.sequence.pad_sequences(problem_sequences, padding='post', maxlen=SEQUENCE_LENGTH, value=-1)
        self.solution_padded = Keras.preprocessing.sequence.pad_sequences(solution_sequences, padding='post', maxlen=SEQUENCE_LENGTH, value=-1)
        print("problem_padded: ", self.problem_padded)
        print("solution_padded: ", self.solution_padded)

        print("Tokens: ", self.tokenizer.get_vocabulary())

    def store(self):
        for i in range(len(self.problem_padded)):
            pFile = open(TOKENIZED_PROBLEMS_LOCATION + str(i) + ".txt", "w")
            sFile = open(TOKENIZED_SUBMISSIONS_LOCATION + str(i) + ".txt", "w")

            for j in range(SEQUENCE_LENGTH):
                pFile.write(str(self.problem_padded[i][j]) + " ")
                sFile.write(str(self.solution_padded[i][j]) + " ")

            pFile.flush()
            sFile.flush()
            pFile.close()
            sFile.close()

        tokenFile = open(TOKEN_FILE_LOCATION, "w")
        json.dump(self.tokenizer.get_vocabulary() , tokenFile, indent=4)
        tokenFile.flush()
        tokenFile.close()

def main():
    load = Load("C:\AIClub\Code\Large Dataset\A_Problems_Clean.json", "C:\AIClub\Code\Large Dataset\A_Submissions_Cleaned")
    load.load_problems()
    load.load_solutions()
    load.tokenize_and_pad()
    load.store()

if __name__ == "__main__":
    main()