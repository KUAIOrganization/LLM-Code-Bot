i, x = input, [0, 0]
n, a = int(i()), [*map(int,i().split())]
for i in range(n):
    b = max(a[0], a[-1])
    x[i % 2] += b
    a.remove(b)
print(*x)