keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

shift = input()
text = input()

for letter in text:
    if shift == "R":
        print(keyboard[keyboard.index(letter) - 1], end="")
    elif shift == "L":
        print(keyboard[keyboard.index(letter) + 1], end="")
