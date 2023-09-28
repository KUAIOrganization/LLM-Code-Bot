a, b = map(int, input().split())
if a % 2 == 0:
    r = a // 2
else:
    r = a // 2 + 1
if b > r:
    b -= r
    print(b * 2)
else:
    print(b * 2 - 1)