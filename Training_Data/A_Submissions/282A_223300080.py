x = 0
for _ in range(int(input())):
    x = x + 1 if '+' in input() else x - 1
print(x)