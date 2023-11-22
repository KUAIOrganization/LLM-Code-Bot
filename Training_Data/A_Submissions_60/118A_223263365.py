# Read input
input_string = input()

# Initialize an empty result string
result_string = ""

# Define a function to check if a character is a vowel
def is_vowel(char):
    return char in "AEIOUYaeiouy"

# Iterate through the input string
for char in input_string:
    if not is_vowel(char):
        # If the character is not a vowel, add a '.' before it and make it lowercase
        result_string += "." + char.lower()

# Print the resulting string
print(result_string)
