n = int(input())
x = 0
for i in range(n):
    val = input()
    if val == 'X++' or val == '++X':
        x += 1
    else:
        #val == 'X--' or val == "--X":
        x -= 1
print(x)