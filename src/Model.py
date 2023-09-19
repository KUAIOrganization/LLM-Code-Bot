import os
import tensorflow as TensorFlow
import tensorflow_text as TensorFlowText #NOT USED BECAUSE UNSUPPORTED ON WINDOWS
from Tokenization.Datastructures.TernarySearchTree import TernarySearchTree
import numpy as Numpy
Keras = TensorFlow.keras

os.environ["KERAS_BACKEND"] = "tensorflow"

# !!! UPDATE THIS IF YOU WANT TO RUN THIS CODE !!!
PATH_TO_SRC = "C:\\AIClub" # Directory that contains the folder 'Code' (and src)

#tokens = ['\n', ' ', '    ', '!', '!=', '%', '(', ')', '):', '*', '**', '+', '+=', '.', '0', '1', '2', '3', '5', ':', '<', '<=', '=', '==', 'M', 'Make', 'P', 'T', 'a', 'an', 'b', 'c', 'checks', 'd', 'def', 'e', 'f', 'g', 'h', 'i', 'if', 'integer', 'is', 'isPrime', 'k', 'l', 'm', 'n', 'number', 'o', 'p', 'prime', 'primeMax', 'primeTest', 'program', 'r', 'return', 's', 't', 'that', 'u', 'w', 'while', 'x']

#The list of tokens this model uses. It is basically just every word and the inputs/outputs used, because it's just four files.
#It was generated using the token generator in Tokenization. The above list (commented out) is the one used before I added the factorization question.
#The indexes of the tokens in this start from 1 because FILLER_TOKEN occupies zero but isn't in the list.
tokens = ['\n', ' ', '    ', '!', '!=', '"', '%', '(', ')', '*', '**', '+', '+=', '-', '.', '0', '1', '2', '3', '5', ':', '<', '<=', '=', '==', 'C', 'Can', 'Cannot', 'E', 'M', 'Make', 'P', 'T', 'V', 'ValueError', 'a', 'b', 'c', 'checks', 'd', 'def', 'e', 'f', 'factorial', 'g', 'h', 'i', 'if', 'integer', 'ints', 'is', 'isPrime', 'k', 'l', 'm', 'n', 'negative', 'not', 'number', 'o', 'of', 'only', 'p', 'prime', 'primeMax', 'primeTest', 'program', 'r', 'raise', 'return', 's', 't', 'take', 'takes', 'that', 'the', 'type', 'u', 'v', 'w', 'while', 'x', 'y']

IN_SIZE = 200 #The max number of tokens in the input
EMBEDDING_HEIGHT = 12 #The number of items in the vectors produced by the embedding layer
FILLER_TOKEN = 0 #Token that is used to fill input to IN_SIZE if it is shorter (should always be zero)
TERMINATE_TOKEN = len(tokens) + 1 #The terminate token 
TOKEN_COUNT = len(tokens) + 2 #The total number of tokens (# in tokens + Filler + Terminate)
# A Ternary search tree that contains all the token strings and their indexes. Ternary search trees are just like binary
# ones except that each node has a middle child. They're good for storing strings. You can look them up for more info.
tree: TernarySearchTree = TernarySearchTree.buildFromOrderedList(tokens, [i for i in range(1, len(tokens) + 1)])

@staticmethod
def tokenize(string: str) -> list[int]:
    """Tokenizes the given string using the tokens in tree.
    
    Turns the string into a list of integers, where each integer corresponds to a character or sequence of
    characters. These integers can be fed into a neural network.
    """
    index = 0
    out: list[int] = []
    while index < len(string):
        pair = getNextToken(string, tree, index)
        if pair[0] == -1:
            break
        out.append(pair[0])
        index = pair[1]
    return out

#out: [value, next index]
@staticmethod
def getNextToken(string: str, tree: TernarySearchTree, index: int) -> list[int]:
    """Gets the next token in the given string, starting at the given index. Returns the token and the index after its end.
    
    Uses the given tree to find the next token in the given string. Searches through the tree and finds the
    longest sequence of characters that has a token and matches the given string, and returns the token of that sequence."""
    built = ""
    if index + 1 == len(string):
        return [-1, -1]
    char = string[index]
    index += 1

    built += char
    result = tree.search(built)

    lastGoodResult = result.value
    lastGoodFileSpot = index
    
    while result.hasChild:
        if index + 1 == len(string):
            break
        char = string[index]
        index += 1
        result = tree.search(built + char)
        if not result.exists:
            return [lastGoodResult, lastGoodFileSpot]
        built += char
        if not(result.value is None):
            lastGoodResult = result.value
            lastGoodFileSpot = index
    
    return [lastGoodResult, lastGoodFileSpot]

@staticmethod
def genDataset(inString: str, outString: str):
    """Given an input and the desired output, returns two lists that can be used to train a model.
    
    Assumes that the input of the model is a sequence of tokens and the output is a one-hot encoding
    of the desired token. 
    Ex: Input = hi, Output = world, tokens = [FILLER_TOKEN, h, i, w, o, r, l, d, TERMINATE_TOKEN], max input length = 10
    Would tokenize each to 128 and 345678.
    It adds a terminate token to the end of the output so that we have a flag to know to stop when we're interpreting its output.
    It adds one to the end of the input too because I think it's good to tell it where the question ends and its response begins.
    The first pair it adds to the dataset would be [1, 2, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]
    The length of the first is 10 because that's the max input length. The length of the second is 9 because that's the number of
    tokens. The second is the one-hot encoding of 3 because when the input is 128(hi), we want the next character to be 3(w)
    The next pair would be [1, 2, 8, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0].
    Now the input is 1283(hi w) and the output is the one-hot of 4(o).
    It repeats this until finally it adds [1, 2, 8, 3, 4, 5, 6, 7, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]"""
    tokensIn = tokenize(inString)
    tokensOut = tokenize(outString)

    tokensIn.append(TERMINATE_TOKEN)
    tokensOut.append(TERMINATE_TOKEN)

    if len(tokensIn) + len(tokensOut) > IN_SIZE:
        raise ValueError("Data size is too large!")

    inBase = Numpy.zeros((IN_SIZE,1), dtype="int32")
    for i in range(len(tokensIn)):
        inBase[i] = tokensIn[i]

    inList = []
    outList = []
    
    index = len(tokensIn)
    for i in range(len(tokensOut)):
        inList.append(inBase.copy())
        out = Numpy.zeros(TOKEN_COUNT)
        out[tokensOut[i]] = 1
        outList.append(out)
        inBase[index + i] = tokensOut[i]

    return (inList, outList)

@staticmethod
def generate(model: Keras.Model, input: str):
    """Given a trained model and an input, returns the model's output.
    
    Does this by giving the model the given input, getting its output (a one-hot encoding of a token),
    and then concatenating the output token onto the input. It does this until either the model outputs a TERMINATE_TOKEN,
    or the input size is greater than IN_SIZE."""
    inputTokenized = tokenize(input)
    inputTokenized.append(TERMINATE_TOKEN)

    inBase = [Numpy.zeros((IN_SIZE,1), dtype="int32")]
    for i in range(len(inputTokenized)):
        inBase[0][i] = inputTokenized[i]

    outToken = None
    outTotal = []

    index = len(inputTokenized)
    while not (outToken == TERMINATE_TOKEN):
        outToken = Numpy.argmax(Numpy.array(model.call(TensorFlow.constant(inBase))))
        inBase[0][index] = outToken
        outTotal.append(outToken)
        index += 1
        if index == IN_SIZE:
            print("Max size reached without end!")
            break

    return detokenize(outTotal)

@staticmethod
def detokenize(tokenList: list[int]):
    """Given a list of tokens, returns the string they represent."""
    out = ""
    for token in tokenList:
        if token == FILLER_TOKEN or token == TERMINATE_TOKEN:
            continue
        out += tokens[token - 1]
    return out

if __name__ == "__main__":    

    # Loads into data1 a dataset with isPrimeQuestion.txt as the input and isPrime.py as the output.
    # Does the same with data2 and the factorials, and concatenates the two datasets into data
    data1 = genDataset(open(os.path.join(PATH_TO_SRC, "Code\\ModelTesting\\isPrimeQuestion.txt")).read(), open(os.path.join(PATH_TO_SRC, "Code\\ModelTesting\\isPrime.py")).read())
    data2 = genDataset(open(os.path.join(PATH_TO_SRC, "Code\\ModelTesting\\factorialQuestion.txt")).read(), open(os.path.join(PATH_TO_SRC, "Code\\ModelTesting\\factorial.py")).read())
    data = (data1[0] + data2[0], data1[1] + data2[1])

    inList = TensorFlow.constant(data[0]) # Creates a tensor of the input dataset
    outList = TensorFlow.constant(data[1]) # Creates a tensor of the output dataset

    dataset = TensorFlow.data.Dataset.from_tensor_slices(data) # Creates a dataset from data. Not used because I have done something wrong and it has too many layers.

    # BUILDING THE MODEL
    # The model is built layer-by-layer. I'll describe each one. You can also look here: https://keras.io/api/layers/

    # This layer is 1 x IN_SIZE. It just takes input. The input is in the form of tokens.
    inputLayer = TensorFlow.keras.Input(shape=(IN_SIZE,), dtype="int32")

    # This layer takes each token and turns it into a vector with dimensions EMBEDDING_HEIGHT x 1. Output dimension is EMBEDDING_HEIGHT x IN_SIZE
    # Each token has its own vector, so it might do [1, 2] -> [[0.1, 0.7], [0.5, 0.2]]
    embeddingLayer = Keras.layers.Embedding(input_dim= TOKEN_COUNT, output_dim=EMBEDDING_HEIGHT, mask_zero=True, input_length=IN_SIZE)(inputLayer)

    # Takes the EMBEDDING_HEIGHT x IN_SIZE rectangle produced by the embedding layer and changes it to EMBEDDING_HEIGHT*IN_SIZE x 1
    reshape = Keras.layers.Reshape((EMBEDDING_HEIGHT * IN_SIZE,))(embeddingLayer)

    # Just an average neural net layer with weights to each of the input nodes and baises and everything. Has size EMBEDDING_HEIGHT*IN_SIZE x 1
    # In some of the text processing examples I found, the layer after the embedding uses the relu activation. I found that to be (very marginally) worse than no activation.
    # That could change for larger models.
    dense1 = Keras.layers.Dense(EMBEDDING_HEIGHT * IN_SIZE)(reshape)

    # This second dense layer didn't really make it preform better, so I removed it
    #dense2 = Keras.layers.Dense(EMBEDDING_HEIGHT * IN_SIZE)(dense1)

    # This is the output layer. It's another dense layer, but it decreases the size to TOKEN_COUNT x 1. It has the softmax activation, so all of its 
    # outputs are probabilities and add up to one.
    dense3 = Keras.layers.Dense(TOKEN_COUNT, activation="softmax")(dense1)

    # Makes the model with input inputLayer and output dense3
    model = TensorFlow.keras.Model(inputLayer, dense3)

    # Compiles the model. The optimizer is just one one of the examples I was looking at used. The categorical crossentropy is supposed
    # to be good for classification tasks with multiple labels and binary outputs. That sounds right for our one-hot outputs. 
    # While it's training, it'll print out the accuracy of the model each epoch.
    model.compile(
        optimizer="rmsprop",
        loss="categorical_crossentropy",
        metrics=["accuracy"])
    
    # Prints a summary describing the structure of the model.
    print(model.summary())

    # Trains the model. Uses inputs from inList, outputs from outList, and 350 epochs. I have found it takes 300-350 epochs for it to 
    # give 100% correct answers pretty consistently.
    out = model.fit(inList, outList, epochs=350, workers = 6, use_multiprocessing=True, batch_size=32)

    print("\n\n")

    # Tests the model with the phrases in each of the question files. 
    print(generate(model, "Make a program that checks if an integer is prime."), "\n")
    print(generate(model, "Make a program that takes the factorial of a number."))