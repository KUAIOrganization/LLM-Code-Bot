n = int(input())
f = [0] + [int(i) for i in input().split()]

found = False

for i in range(1, n + 1):
    if f[f[f[i]]] == i:
        found = True

result = 'YES' if found else 'NO'
print(result)
