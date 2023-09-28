n = int(input())
pack = []
if n % 2 == 0:
    x = n // 2
    print(x)
    for _ in range(x):
        pack.append("2")
    print(*pack)
else:
    x = n // 2
    print(x)
    for _ in range(x-1):
        pack.append("2")
    print(*pack, '3')