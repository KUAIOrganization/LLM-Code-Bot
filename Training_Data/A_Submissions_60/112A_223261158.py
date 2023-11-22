# https://codeforces.com/problemset/problem/112/A

def solve(word1, word2):
    response = 0
    i = 0
    while i<len(word1) and response == 0:
        if word1[i] < word2[i]:
            response = -1
        if word1[i] > word2[i]:
            response = 1
        i += 1
    return response

word1 = input()
word2 = input()

print(solve(word1.lower(), word2.lower()))
