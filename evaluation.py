import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import tensorflow as tf

from Transformer import Transformer, EncoderLayer, DecoderLayer, TransformerEncoder, TransformerDecoder, ModelArgs


class Evaluator:
    def __init__(self, model, problem_tokenizer, solution_tokenizer, log_dir):
        self.model = model
        self.problem_tokenizer = problem_tokenizer
        self.solution_tokenizer = solution_tokenizer
        self.writer = tf.summary.create_file_writer(log_dir)

    def log_vocabulary(self):
        with self.writer.as_default():
            for word, index in self.problem_tokenizer.word_index.items():
                tf.summary.text(name="Problem Vocabulary", data=f"{word}: {index}", step=0)

            for word, index in self.solution_tokenizer.word_index.items():
                tf.summary.text(name="Solution Vocabulary", data=f"{word}: {index}", step=0)

            self.writer.flush()

    def _log_dataset_samples(self, problems, decoder_inputs, targets):
        with self.writer.as_default():
            for i, (problem, decoder_input, target) in enumerate(zip(problems, decoder_inputs, targets)):
                if i >= 5:  # Log 5 samples
                    break
                
                problem_text = self.problem_tokenizer.sequences_to_texts([problem.numpy()])
                decoder_input_text = self.solution_tokenizer.sequences_to_texts([decoder_input.numpy()])
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
        plt.show()

    def plot_token_probabilities(self, token_index, n_samples=1):
        for (encoder_input, decoder_input), _ in self.dataset.take(1):
            encoder_input = encoder_input[:n_samples]
            decoder_input = decoder_input[:n_samples]

            predictions = self.model.predict([encoder_input, decoder_input])

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
                plt.show()

    def generate_training_predictions(self, dataset, n_samples=1):
        for (encoder_inputs, decoder_inputs), _ in dataset.take(1):
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

    def generate_manual_predictions(self, input_text, max_length_input):
        input_seq = self.problem_tokenizer.texts_to_sequences([input_text])
        input_padded = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=max_length_input, padding='post')

        start_token_index = self.solution_tokenizer.word_index.get('[START]', 1)
        decoder_input = np.array([[start_token_index]])

        predictions = self.model.predict([input_padded, decoder_input])
        predicted_sequence = np.argmax(predictions, axis=-1)[0]
        predicted_text = self.solution_tokenizer.sequences_to_texts([predicted_sequence])

        print("Input text:", input_text)
        print("Predicted text:", predicted_text[0])

    def evaluate(self, command, *args, **kwargs):
        if command == 'loss':
            self.plot_loss(*args, **kwargs)
        elif command == 'token_prob':
            self.plot_token_probabilities(*args, **kwargs)
        elif command == 'training_sample_pred':
            self.generate_training_predictions(*args, **kwargs)
        elif command == 'manual_sample_pred':
            self.generate_manual_predictions(*args, **kwargs)
        else:
            print(f"Unknown command: {command}")


# Load model and tokenizers
base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(base_dir, "Transformer", "model_files")

# Ensure to load the model with custom objects if necessary
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

# Create an instance of Evaluator
evaluator = Evaluator(model, problem_tokenizer, solution_tokenizer, log_dir)

# Example usage
input_text = "Print the numbers 1-9"
evaluator.evaluate('manual_sample_pred', input_text, max_length_input=50)

input_text = "Print the numbers 1-9"
evaluator.evaluate('manual_sample_pred', input_text, max_length_input=50)