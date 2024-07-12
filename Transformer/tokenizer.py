# workspace/Transformer/tokenizer.py

import io
import os
import pickle
import tokenize

from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore


class Tokenizers:
    def __init__(self, base_dir):
        # For saving in pickles
        self.base_dir = base_dir
        self.problem_tokenizer_dir = os.path.join(base_dir, 'problem_tokenizer.pkl')
        self.solution_tokenizer_dir = os.path.join(base_dir, 'solution_tokenizer.pkl')

        # For saving metadata for embedding projection
        metadata_dir = os.path.join(base_dir, 'metadata')
        self.problem_metadata_path = os.path.join(metadata_dir, 'problem_metadata.tsv')
        self.solution_metadata_path = os.path.join(metadata_dir, 'solution_metadata.tsv')
        os.makedirs(metadata_dir, exist_ok=True)

        # Instantiate keras tokenizer
        self.problem_tokenizer = Tokenizer(filters='', oov_token='UNK')
        self.solution_tokenizer = Tokenizer(filters='', oov_token='UNK', lower=False)

        self.sos_token = '<SOS>'
        self.eos_token = '<EOS>'

    def save_metadata(self, tokenizer, metadata_path):
        print("metadata path:", metadata_path)
        with open(metadata_path, 'w') as f:
            for word, index in tokenizer.word_index.items():
                f.write(f'{word}\n')
    
    def tokenize_input(self, problems):
        # Fit Keras tokenizer
        self.problem_tokenizer.fit_on_texts(problems)

        # Save tokenizer
        with open(self.problem_tokenizer_dir, 'wb') as f:
            pickle.dump(self.problem_tokenizer, f)

        self.save_metadata(self.problem_tokenizer, self.problem_metadata_path)

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
            for token in tokenize.generate_tokens(io.StringIO(solution).readline):
                tokens.append(token.string)
            decoder_inputs.append([self.sos_token] + tokens)
            targets.append(tokens + [self.eos_token])
        
        # Fit Keras tokenizer and tokenize
        self.solution_tokenizer.fit_on_texts([[self.sos_token, self.eos_token]] + decoder_inputs + targets)

        # Save tokenizer
        with open(self.solution_tokenizer_dir, 'wb') as f:
            pickle.dump(self.solution_tokenizer, f)

        self.save_metadata(self.solution_tokenizer, self.solution_metadata_path)

        # Tokenize with Keras tokenizer
        decoder_inputs = self.solution_tokenizer.texts_to_sequences(decoder_inputs)
        targets = self.solution_tokenizer.texts_to_sequences(targets)

        # Pad
        max_length_output = max(len(seq) for seq in targets)
        decoder_inputs = pad_sequences(decoder_inputs, padding='post', maxlen=max_length_output)
        targets = pad_sequences(targets, padding='post', maxlen=max_length_output)

        return decoder_inputs, targets