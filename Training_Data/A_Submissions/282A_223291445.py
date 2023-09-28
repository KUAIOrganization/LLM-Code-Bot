n = int(input())
x = 0
for i in range(n):
    state = input()
    if '+' in state:
        x += 1
    else:
        x -= 1
print(x)