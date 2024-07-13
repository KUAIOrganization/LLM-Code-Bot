# workspace/evaluation.py

import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import tensorflow as tf

from Transformer import Transformer, EncoderBlock, DecoderBlock


class Evaluator:
    def __init__(self, model, dataset_path, problem_tokenizer, solution_tokenizer, log_dir):
        self.model = model
        self.dataset_path = dataset_path
        self.problem_tokenizer = problem_tokenizer
        self.solution_tokenizer = solution_tokenizer
        self.writer = tf.summary.create_file_writer(log_dir)

    def get_dataset(self, num_samples=10):
        # Load
        df = pd.read_csv(self.dataset_path)
        encoder_inputs = df['encoder_inputs'].apply(eval).tolist()
        decoder_inputs = df['decoder_inputs'].apply(eval).tolist()
        
        dataset = tf.data.Dataset.from_tensor_slices((encoder_inputs, decoder_inputs))
        
        # Print
        for (enc_input, dec_input) in dataset.take(num_samples):
            print(f"Encoder Input: {enc_input.numpy()[:10]}")
            print(f"Decoder Input: {dec_input.numpy()[:10]}")
        
        return dataset

    def log_vocabulary(self):
        with self.writer.as_default():
            for word, index in self.problem_tokenizer.word_index.items():
                tf.summary.text(name="Problem Vocabulary", data=f"{word}: {index}", step=0)

            for word, index in self.solution_tokenizer.word_index.items():
                tf.summary.text(name="Solution Vocabulary", data=f"{word}: {index}", step=0)

            self.writer.flush()

    def _log_dataset_samples(self, problems, decoder_inputs, targets):
        with self.writer.as_default():
            for i, (problem, decoder_inputs, target) in enumerate(zip(problems, decoder_inputs, targets)):
                if i >= 5: # Log 5 samples
                    break
                
                problem_text = self.problem_tokenizer.sequences_to_texts([problem.numpy()])
                decoder_input_text = self.solution_tokenizer.sequences_to_texts([decoder_inputs.numpy()])
                target_text = self.solution_tokenizer.sequences_to_texts([target.numpy()])

                tf.summary.text(name=f"problem_{i}", data=problem_text, step=0)
                tf.summary.text(name=f"decoder_input_{i}", data=decoder_input_text, step=0)
                tf.summary.text(name=f"target_{i}", data=target_text, step=0)

            self.writer.flush()

    def plot_loss(self, history):
        plt.figure(figsize=(10, 6))
        plt.plot(history.history['loss'])
        plt.title('Loss Curve')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.savefig(f'loss.png')
        plt.close()

    def inference_training_data(self, n_samples=1):
        dataset = self.get_dataset(num_samples=n_samples)
        for (encoder_inputs, decoder_inputs) in dataset.take(n_samples):
            encoder_inputs = np.expand_dims(encoder_inputs, axis=0)
            decoder_inputs = np.expand_dims(decoder_inputs, axis=0)

            predictions = self.model.predict((encoder_inputs, decoder_inputs))
            predicted_sequences = np.argmax(predictions, axis=-1)

            input_texts = self.problem_tokenizer.sequences_to_texts(encoder_inputs.tolist())
            predicted_texts = self.solution_tokenizer.sequences_to_texts(predicted_sequences)

            for i, predicted_text in enumerate(predicted_texts):
                print(f"Sample {i + 1}:")
                print("Input sequence [:50]:", input_texts[i][:50])
                print("Predicted sequence:", predicted_sequences[i][:50])
                print("Predicted text:", predicted_text[:50], "\n")

    def inference(self, input_text, max_length_input):
        input_seq = self.problem_tokenizer.texts_to_sequences([input_text])
        print("input seq:", input_seq)
        input_padded = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=max_length_input, padding='post')

        start_token_index = self.solution_tokenizer.word_index.get('<SOS>', 1)
        decoder_inputs = np.array([[start_token_index]])

        predictions = self.model.predict([input_padded, decoder_inputs])
        predicted_sequence = np.argmax(predictions, axis=-1)[0]
        predicted_text = self.solution_tokenizer.sequences_to_texts([predicted_sequence])

        print("Input text:", input_text)
        print(predicted_text)
        print("Predicted text:", predicted_text[0])


# Load model and tokenizers
base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(base_dir, "Transformer", "model_files")
dataset_dir = os.path.join(base_dir, 'Training_Data', 'All')
dataset_path = os.path.join(dataset_dir, "tokenized_padded_data.csv")
problem_tokenizer_path = os.path.join(dataset_dir, 'problem_tokenizer.pkl')
solution_tokenizer_path = os.path.join(dataset_dir, 'solution_tokenizer.pkl')
log_dir = os.path.join(base_dir, "logs", "run_" + datetime.datetime.now().strftime("%m_%d_%H_%M"))

model = tf.keras.models.load_model(
    f"{model_dir}/checkpoint.keras",
    custom_objects={
        'EncoderBlock': EncoderBlock,
        'DecoderBlock': DecoderBlock, 
        'Transformer': Transformer
    }
)

with open(problem_tokenizer_path, 'rb') as f:
    problem_tokenizer = pickle.load(f)
with open(solution_tokenizer_path, 'rb') as f:
    solution_tokenizer = pickle.load(f)

# Call this evaluator instance
evaluator = Evaluator(model, dataset_path, problem_tokenizer, solution_tokenizer, log_dir)

# Dataset overfit prediction
evaluator.inference_training_data(n_samples=2)

# Manual prediction
input_text = "Write a NumPy program to repeat elements of an array. "
evaluator.inference(input_text, max_length_input=50)

# def print_model_layers(object):
#     if hasattr(object, 'layers'):
#         print(f"{object.name} has sublayers {[layer.name for layer in object.layers]}")
#         for layer in object.layers:
#             print_model_layers(layer)
# print_model_layers(model)