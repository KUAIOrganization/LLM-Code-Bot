# workspace/evaluation.py

import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import tensorflow as tf

from Transformer import Transformer, EncoderLayer, DecoderLayer, TransformerEncoder, TransformerDecoder, ModelArgs


class Evaluator:
    def __init__(self, model, dataset_path, problem_tokenizer, solution_tokenizer, log_dir):
        self.model = model
        self.dataset_path = dataset_path
        self.problem_tokenizer = problem_tokenizer
        self.solution_tokenizer = solution_tokenizer
        self.writer = tf.summary.create_file_writer(log_dir)

    def load_and_print_dataset_tokens(self, num_samples=10):
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
                if i >= 5:  # Log 5 samples
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

    def plot_token_probabilities(self, token_index, n_samples=1):
        dataset = self.load_and_print_dataset_tokens(num_samples=n_samples)
        for (encoder_inputs, decoder_inputs) in dataset.take(n_samples):
            encoder_inputs = tf.reshape(encoder_inputs, (1, -1))
            decoder_inputs = tf.reshape(decoder_inputs, (1, -1))

            predictions = self.model.predict([encoder_inputs, decoder_inputs])

            for sample_idx in range(n_samples):
                token_logits = predictions[sample_idx, token_index, :]
                token_probabilities = tf.nn.softmax(token_logits).numpy()
                sorted_indices = np.argsort(token_probabilities)[::-1]
                sorted_probabilities = token_probabilities[sorted_indices]

                plt.figure(figsize=(20, 5))
                plt.bar(range(len(sorted_probabilities)), sorted_probabilities)
                plt.xlabel('Word Indices (sorted by probability)')
                plt.ylabel('Probability')
                plt.title(f'Word Prediction Probabilities for Token {token_index} in Sample {sample_idx+1}')
                plt.savefig(f'token_probabilities_{token_index}.png')
                plt.close()

    def inference_training_data(self, n_samples=1):
        dataset = self.load_and_print_dataset_tokens(num_samples=n_samples)
        for (encoder_inputs, decoder_inputs) in dataset.take(n_samples):
            encoder_inputs = encoder_inputs[:n_samples]
            decoder_inputs = decoder_inputs[:n_samples]

            predictions = self.model.predict([encoder_inputs, decoder_inputs])
            predicted_sequences = np.argmax(predictions, axis=-1)

            input_texts = self.problem_tokenizer.sequences_to_texts(encoder_inputs.numpy())
            predicted_texts = self.solution_tokenizer.sequences_to_texts(predicted_sequences)

            for i, predicted_text in enumerate(predicted_texts):
                print(f"Sample {i + 1}:")
                print("Input sequence [:250]:", input_texts[i][:250])
                print("Predicted sequence:", predicted_sequences[i])
                print("Predicted text:", predicted_text, "\n")

    def inference(self, input_text, max_length_input):
        input_seq = self.problem_tokenizer.texts_to_sequences([input_text])
        input_padded = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=max_length_input, padding='post')

        start_token_index = self.solution_tokenizer.word_index.get('[START]', 1)
        decoder_inputs = np.array([[start_token_index]])

        predictions = self.model.predict([input_padded, decoder_inputs])
        predicted_sequence = np.argmax(predictions, axis=-1)[0]
        predicted_text = self.solution_tokenizer.sequences_to_texts([predicted_sequence])

        print("Input text:", input_text)
        print(predicted_text)
        print("Predicted text:", predicted_text[0])

    def evaluate(self, command, *args, **kwargs):
        if command == 'loss':
            self.plot_loss(*args, **kwargs)
        elif command == 'token_prob':
            self.plot_token_probabilities(*args, **kwargs)
        elif command == 'training_sample_pred':
            self.inference_training_data(*args, **kwargs)
        elif command == 'manual_sample_pred':
            self.inference(*args, **kwargs)
        else:
            print(f"Unknown command: {command}")


# Load model and tokenizers
base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(base_dir, "Transformer", "model_files")
dataset_path = os.path.join(base_dir, "Training_Data", "All", "tokenized_padded_data.csv")

model = tf.keras.models.load_model(
    f"{model_dir}/model.keras",
    custom_objects={
        'Transformer': Transformer,
        'EncoderLayer': EncoderLayer,
        'DecoderLayer': DecoderLayer,
        'TransformerEncoder': TransformerEncoder,
        'TransformerDecoder': TransformerDecoder,
        'ModelArgs': ModelArgs
    }
)

with open(f"{model_dir}/problem_tokenizer.pkl", 'rb') as f:
    problem_tokenizer = pickle.load(f)
with open(f"{model_dir}/solution_tokenizer.pkl", 'rb') as f:
    solution_tokenizer = pickle.load(f)

log_dir = os.path.join(base_dir, "logs", "run_" + datetime.datetime.now().strftime("%m_%d_%H_%M"))

# Call this evaluator instance
evaluator = Evaluator(model, dataset_path, problem_tokenizer, solution_tokenizer, log_dir)

# From training data
# input_text = "Write a NumPy program to repeat elements of an array. "
# evaluator.evaluate('inference', input_text, max_length_input=50)

evaluator.evaluate('token_prob', 1)