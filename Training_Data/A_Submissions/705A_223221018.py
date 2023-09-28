num = int(input())
word = []
for x in range(num):
    if x % 2 == 0:
        word.append('I hate')
    else:
        word.append('I love')
print(' that '.join(word) + ' it')