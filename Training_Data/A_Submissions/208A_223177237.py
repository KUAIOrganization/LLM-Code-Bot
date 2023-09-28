s = input()
words = [word for word in s.split("WUB") if word != ""]

original_song = " ".join(words)

print(original_song)
