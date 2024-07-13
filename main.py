# workspace/main.py

import datetime
import os
import pickle
import tensorflow as tf

from Transformer import (
    Dataset_Generator, ModelArgs, 
    Transformer, EncoderBlock, DecoderBlock, EncoderLayer, DecoderLayer, NoamSchedule, 
    Codeforces_A, LeetCode_Complete, LeetCode_Master, LeetCode_Train, Problem_Solution, All
)


class FullWeightHistCallback(tf.keras.callbacks.Callback):
    """Callback to save histograms of every trainable model weight"""

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
    """Callback to test quality of specific outputs and health of probability distribution"""

    def __init__(self, save_freq, log_dir, problem_tokenizer, solution_tokenizer, sample_encoder_input, sample_decoder_input):
        super().__init__()
        self.save_freq = save_freq
        self.file_writer = tf.summary.create_file_writer(log_dir)
        self.problem_tokenizer = problem_tokenizer
        self.solution_tokenizer = solution_tokenizer

        self.sample_encoder_input = self.preprocess_string(sample_encoder_input)
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
        if (epoch+1)%self.save_freq == 0:
            predictions = self.model.predict((self.sample_encoder_input, self.sample_decoder_input))
            token_probs = tf.nn.softmax(predictions, axis=-1)
            with self.file_writer.as_default():
                filtered_probs = tf.boolean_mask(token_probs, token_probs > 0.01) # Trim down
                tf.summary.histogram(f"token_probabilities", filtered_probs, step=epoch)
                
                token_prob = tf.reduce_mean(token_probs[:, :, self.example_index_1])
                tf.summary.scalar(f"token_probabilities/{self.example_word_1}", token_prob, step=epoch)

                token_prob = tf.reduce_mean(token_probs[:, :, self.example_index_2])
                tf.summary.scalar(f"token_probabilities/{self.example_word_2}", token_prob, step=epoch)


class ModelSaveCallback(tf.keras.callbacks.Callback):
    """Callback to save the model to a checkpoint"""

    def __init__(self, save_freq, save_path):
        super(ModelSaveCallback, self).__init__()
        self.save_freq = save_freq
        self.save_path = save_path
    
    def on_epoch_end(self, epoch, logs=None):
        if (epoch+1) % self.save_freq == 0:
            self.model.save(self.save_path)
            print(f"\nSaved model checkpoint for epoch {epoch+1}")


def set_gpu_config():
    """Ensure GPU is available and enable memory growth"""
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            tf.config.set_visible_devices(gpus[0], 'GPU')
            print(f"Using GPU: {gpus[0]}")
        except RuntimeError as error:
            print(error)
    else:
        print("No GPU found")
        input("Press enter to continue without GPU")


def print_model_layers(object):
    """Recursively print the model structure"""
    if hasattr(object, 'layers'):
        print(f"{object.name} has sublayers {[layer.name for layer in object.layers]}")
        for layer in object.layers:
            print_model_layers(layer)


def set_hyperparameters():
    """Set and return model hyperparameters"""
    args = ModelArgs()
    return args


def generate_dataset(base_dir, dataset_choice, args):
    """Generate the chosen dataset with args.batch_size"""
    generator = Dataset_Generator(base_dir, dataset_choice.base_dir)
    generate_function = generator.get_generate_function(dataset_choice)
    generate_function()
    dataset = dataset_choice.create_dataset(args.batch_size)

    print("Dataset element_spec:", dataset.element_spec)
    return generator, dataset


def load_tokenizers(generator, args):
    """Load tokenizers and update args vocabulary sizes"""
    with open(generator.tokenizer.problem_tokenizer_path, 'rb') as f:
        problem_tokenizer = pickle.load(f)
        args.problem_vocab_size = len(problem_tokenizer.word_index) + 1

    with open(generator.tokenizer.solution_tokenizer_path, 'rb') as f:
        solution_tokenizer = pickle.load(f)
        args.solution_vocab_size = len(solution_tokenizer.word_index) + 1

    return problem_tokenizer, solution_tokenizer


def build_model(model_path, checkpoint_path, args, from_checkpoint):
    """Build or load the model based on the from_checkpoint flag"""
    if from_checkpoint:
        model = tf.keras.models.load_model(
            checkpoint_path, 
            custom_objects={
                'Transformer': Transformer, 
                'EncoderBlock': EncoderBlock,
                'DecoderBlock': DecoderBlock, 
                'EncoderLayer': EncoderLayer, 
                'DecoderLayer': DecoderLayer, 
                'NoamSchedule': NoamSchedule
            }
        )
        print(f"Loaded model from checkpoint {checkpoint_path}")
    else:
        encoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='encoder_input')
        decoder_input = tf.keras.Input(shape=(None,), dtype='int32', name='decoder_input')

        model = Transformer(args)
        model((encoder_input, decoder_input))
        print(f"Loaded new model to save at {model_path}")

    model.compile()
    return model


def main():
    """Main function to set up, train, and save the model"""
    set_gpu_config() # Ensure GPU is enabled with memory growth

    # Set paths
    base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))

    model_dir = os.path.join(base_dir, "Transformer", "model_files")
    model_path = os.path.join(model_dir, "trained_model.keras")
    checkpoint_path = os.path.join(model_dir, "checkpoint.keras")

    time = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%m%d_%H%M")
    base_log_dir = os.path.join(base_dir, 'logs', 'run_' + time)
    fit_log_dir = os.path.join(base_log_dir, 'fit')
    
    # Generate the dataset
    args = set_hyperparameters()
    dataset_choice = All # [All, Codeforces_A, LeetCode_Complete, LeetCode_Master, LeetCode_Train, Problem_Solution]
    generator, dataset = generate_dataset(base_dir, dataset_choice, args)

    # Load tokenizers
    problem_tokenizer, solution_tokenizer = load_tokenizers(generator, args)

    # Build the model
    model = build_model(model_path, checkpoint_path, args, from_checkpoint=False)
    # model.summary()
    # print_model_layers(model)
    # exit()

    # Callbacks
    # metadata_dir = os.path.join(dataset_choice.base_dir, 'metadata')
    projector_dir = os.path.join(dataset_choice.base_dir, 'embeddings')
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=fit_log_dir, histogram_freq=1, embeddings_freq=1, 
        embeddings_metadata={
            'problem_embedding': os.path.join(projector_dir, 'problem_metadata.tsv'), 
            'solution_embedding': os.path.join(projector_dir, 'solution_metadata.tsv')
        }
    )
    weight_callback = FullWeightHistCallback(save_freq=3, log_dir=fit_log_dir, include_biases=True)
    sample_encoder_input = ["Using python, write a for loop that prints 10 numbers."]
    sample_decoder_input = ["for i in range("]
    token_prob_callback = TokenProbabilityCallback(5, fit_log_dir, problem_tokenizer, solution_tokenizer, sample_encoder_input, sample_decoder_input)
    checkpoint_callback = ModelSaveCallback(save_freq=10, save_path=checkpoint_path)
    
    # Train the model
    history = model.fit(
        dataset, 
        epochs=args.epochs, 
        callbacks=[checkpoint_callback, weight_callback, token_prob_callback, tensorboard_callback]
    )
    
    # Save the model
    model.save(model_path)

if __name__ == '__main__':
    main()

    # print("Get build info", tf.sysconfig.get_build_info())
    # print("tf version:", tf.__version__)
    # print("cudnn version:", tf.sysconfig.get_build_info()["cudnn_version"])
    # print("cuda version:", tf.sysconfig.get_build_info()["cuda_version"])
    # print("Num GPUs Available: ", tf.config.list_physical_devices())