#!/usr/bin/env python
# coding: utf-8


import datetime
import os

import tensorflow as tf
import pickle

from Transformer import ModelArgs, Dataset_Generator, build_and_compile, Codeforces_A, Problem_Solution, All


def main():
    # Use environment variable if set
    base_dir = os.getenv('WORKSPACE_DIR', os.path.dirname(os.path.abspath(__file__)))
    base_log_dir = os.path.join(base_dir, 'logs', 'run_' + datetime.datetime.now().strftime('%m_%d_%H_%M'))
    fit_log_dir = os.path.join(base_log_dir, 'fit')
    debug_log_dir = os.path.join(base_log_dir, 'debug')

    """Enable full debugging
    # Enable full debugging
    #tf.config.optimizer.set_jit(False)  # Disable XLA compilation
    tf.config.run_functions_eagerly(True)
    tf.data.experimental.enable_debug_mode() # Disables tf.data eager execution; not covered by run_functions_eagerly

    tf.debugging.experimental.enable_dump_debug_info(
        debug_log_dir,
        tensor_debug_mode="NO_TENSOR", # CONCISE_HEALTH
        circular_buffer_size=1000) # 1000
    """
    
    args = ModelArgs()
    
    # Generate the dataset
    dataset_choice = Problem_Solution # [All, Codeforces_A, Problem_Solution]
    reduced = True # If you want to use a small dataset

    args.input_seq_length = dataset_choice.reduced_length_input if reduced else dataset_choice.max_length_input
    args.output_seq_length = dataset_choice.reduced_length_output if reduced else dataset_choice.max_length_output
    
    if not os.path.exists(dataset_choice.tokenized_path):
        generator = Dataset_Generator(base_dir)
        load_function = generator.get_load_function(dataset_choice)
        load_function()

    dataset_choice.create_dataset(args.batch_size, reduced)
    
    # Load tokenizer information
    with open('Transformer/model_files/problem_tokenizer.pkl', 'rb') as f:
        problem_tokenizer = pickle.load(f)
        args.problem_vocab_size = len(problem_tokenizer.word_index) + 1

    with open('Transformer/model_files/solution_tokenizer.pkl', 'rb') as f:
        solution_tokenizer = pickle.load(f)
        args.solution_vocab_size = len(solution_tokenizer.word_index) + 1
    
    # Build the model
    model = build_and_compile(args)
    
    # Setup TensorBoard callback
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=fit_log_dir, histogram_freq=1)
    
    # Train the model
    history = model.fit(dataset_choice.dataset, epochs=args.epochs, callbacks=[tensorboard_callback]) # history variable unused...
    
    # Save the model
    model_dir = os.path.join(base_dir, "Transformer", "model_files")
    model.save(os.path.join(model_dir, "model.keras"))

if __name__ == '__main__':
    """Miscellaneous functions to run
    """
    #tf.config.run_functions_eagerly(True)
    #tf.data.experimental.enable_debug_mode()
    #tf.executing_eagerly()

    main()

    #print(len(loader.problem_tokenizer.word_index) + 1)
    #print(len(loader.solution_tokenizer.word_index) + 1)

    # Clears logs folder
    #!find logs -mindepth 1 -delete

    #tf.debugging.experimental.disable_dump_debug_info()

    #!kill 415

    #print("hello")

    #print(tf.sysconfig.get_build_info())

    #print(tf.__version__)

    #print(tf.sysconfig.get_build_info()["cuda_version"])
    #print(tf.sysconfig.get_build_info()["cudnn_version"])

    #!pip install --upgrade tensorflow
    #!pip install --upgrade tensorboard