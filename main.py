# workspace/main.py

import datetime
import os
import pickle
import tensorflow as tf

from Transformer import ModelArgs, Dataset_Generator, build_and_compile
from Transformer import Codeforces_A, LeetCode_Complete, LeetCode_Master, LeetCode_Train, Problem_Solution, All


class FullWeightHistCallback(tf.keras.callbacks.Callback):
    def __init__(self, save_freq, log_dir, include_biases):
        super(FullWeightHistCallback, self).__init__()
        self.file_writer = tf.summary.create_file_writer(log_dir)
        self.save_freq = save_freq
        self.include_biases = include_biases

    def save_histograms(self, epoch):
        if (epoch+1) % self.save_freq:
            with self.file_writer.as_default():
                for layer in self.model.layers:
                    self.log_layer_histograms(layer, epoch) # Recursive
            self.file_writer.flush()
    
    def log_layer_histograms(self, layer, epoch):
        if hasattr(layer, 'layers'):
            for sublayer in layer.layers:
                self.log_layer_histograms(sublayer, epoch)
        elif hasattr(layer, 'weights'):
            for weight in layer.weights:
                if 'bias' not in weight.name or self.include_biases:
                    tf.summary.histogram(f"Weights/{layer.name}", weight, step=epoch)

    def on_epoch_end(self, epoch, logs=None):
        self.save_histograms(epoch)

class TokenProbabilityCallback(tf.keras.callbacks.Callback):
    def __init__(self, log_dir, problem_tokenizer, solution_tokenizer, sample_encoder_input, sample_decoder_input):
        super().__init__()
        self.file_writer = tf.summary.create_file_writer(log_dir)
        self.problem_tokenizer = problem_tokenizer
        self.solution_tokenizer = solution_tokenizer

        self.sample_encoder_input = self.preprocess_string(sample_decoder_input)
        self.sample_decoder_input = self.preprocess_string(sample_decoder_input)

        self.example_word_1 = "10"
        self.example_word_2 = "<EOS>"
        self.example_index_1 = self.get_token_indices(self.example_word_1)
        self.example_index_2 = self.get_token_indices(self.example_word_2)

    def preprocess_string(self, input_string):
        tokenized_input = self.problem_tokenizer.texts_to_sequences(input_string)
        tensor_input = tf.convert_to_tensor(tokenized_input)
        return tensor_input

    def get_token_indices(self, word):
        index = self.solution_tokenizer.word_index.get(word)
        print(f"TokenProbabilityCallback example word {word}: {index}")
        return index

    def on_epoch_end(self, epoch, logs=None):
        predictions = self.model.predict([self.sample_encoder_input, self.sample_decoder_input])
        token_probs = tf.nn.softmax(predictions, axis=-1)
        with self.file_writer.as_default():
            filtered_probs = tf.boolean_mask(token_probs, token_probs > 0.01) # Trim down
            tf.summary.histogram(f"token_probabilities", filtered_probs, step=epoch)
            
            token_prob = tf.reduce_mean(token_probs[:, :, self.example_index_1])
            tf.summary.scalar(f"token_probabilities/{self.example_word_1}", token_prob, step=epoch)

            token_prob = tf.reduce_mean(token_probs[:, :, self.example_index_2])
            tf.summary.scalar(f"token_probabilities/{self.example_word_2}", token_prob, step=epoch)

class ModelSaveCallback(tf.keras.callbacks.Callback):
    def __init__(self, save_freq, save_path):
        super(ModelSaveCallback, self).__init__()
        self.save_freq = save_freq
        self.save_path = save_path
    
    def on_epoch_end(self, epoch, logs=None):
        if (epoch+1) % self.save_freq == 0:
            self.model.save(self.save_path)
            print(f"\nSaved model checkpoint for epoch {epoch+1}")

def set_gpu_config():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            tf.config.set_visible_devices(gpus[0], 'GPU')
            print(f"Using GPU: {gpus[0]}")
        except RuntimeError as e:
            print(e)

def main():
    set_gpu_config()

    # Set paths
    base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))

    model_dir = os.path.join(base_dir, "Transformer", "model_files")
    model_path = os.path.join(model_dir, "trained_model.keras")
    checkpoint_path = os.path.join(model_dir, "checkpoint.keras")

    time = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%m%d_%H%M")
    base_log_dir = os.path.join(base_dir, 'logs', 'run_' + time)
    fit_log_dir = os.path.join(base_log_dir, 'fit')

    # Set hyperparameters
    args = ModelArgs()
    
    # Generate the dataset
    dataset_choice = All # [All, Codeforces_A, LeetCode_Complete, LeetCode_Master, LeetCode_Train, Problem_Solution]

    # if not os.path.exists(dataset_choice.tokenized_path):
    generator = Dataset_Generator(base_dir, dataset_choice.base_dir)
    generate_function = generator.get_generate_function(dataset_choice)
    generate_function()

    dataset = dataset_choice.create_dataset(args.batch_size)
    print("Dataset element_spec:", dataset.element_spec)

    # Load tokenizers
    with open('Transformer/model_files/problem_tokenizer.pkl', 'rb') as f:
        problem_tokenizer = pickle.load(f)
        args.problem_vocab_size = len(problem_tokenizer.word_index) + 1

    with open('Transformer/model_files/solution_tokenizer.pkl', 'rb') as f:
        solution_tokenizer = pickle.load(f)
        args.solution_vocab_size = len(solution_tokenizer.word_index) + 1

    # Build the model
    from_checkpoint = False # True, False
    if from_checkpoint:
        print(f"Loaded model from checkpoint {checkpoint_path}")
        model = tf.keras.models.load_model(checkpoint_path)
    else:
        print(f"Loaded new model to save at {model_path}")
        model = build_and_compile(args)
    model.summary()

    # Callbacks
    # tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=fit_log_dir, histogram_freq=1, embeddings_freq=1)
    # metadata_dir = os.path.join(dataset_choice.base_dir, 'metadata')
    projector_dir = os.path.join(dataset_choice.base_dir, 'embeddings')
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=fit_log_dir, histogram_freq=1, embeddings_freq=1, 
        embeddings_metadata={
            'problem_embedding': os.path.join(projector_dir, 'problem_metadata.tsv'), 
            'solution_embedding': os.path.join(projector_dir, 'solution_metadata.tsv')
        }
    )
    weight_callback = FullWeightHistCallback(save_freq=2, log_dir=fit_log_dir, include_biases=True)
    sample_encoder_input = ["Using python, write a for loop that prints 10 numbers."]
    sample_decoder_input = ["for i in range("]
    token_prob_callback = TokenProbabilityCallback(fit_log_dir, problem_tokenizer, solution_tokenizer, sample_encoder_input, sample_decoder_input)
    checkpoint_callback = ModelSaveCallback(save_freq=10, save_path=checkpoint_path)
    
    # Train the model
    history = model.fit(
        dataset, 
        epochs=args.epochs, 
        callbacks=[tensorboard_callback, checkpoint_callback, weight_callback, token_prob_callback])
    
    # Save the model
    model.save(model_path)

if __name__ == '__main__':
    main()

    # Clears logs folder
    #!find logs -mindepth 1 -delete

    #tf.debugging.experimental.disable_dump_debug_info()

    #!kill 415

    # print("Get build info", tf.sysconfig.get_build_info())

    # print("tf version:", tf.__version__)

    # print("cudnn version:", tf.sysconfig.get_build_info()["cudnn_version"])
    # print("cuda version:", tf.sysconfig.get_build_info()["cuda_version"])
    # print("Num GPUs Available: ", tf.config.list_physical_devices())