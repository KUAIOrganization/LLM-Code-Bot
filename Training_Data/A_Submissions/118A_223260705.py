#https://codeforces.com/problemset/problem/118/A

word = str(input())
word = word.lower()
word_len = len(word)
vowles = ["a", "o", "y", "e", "u", "i"]
output= ""

for i in range(0, word_len):
    if word[i] not in vowles:
        output += "."+ word[i]

print(output)