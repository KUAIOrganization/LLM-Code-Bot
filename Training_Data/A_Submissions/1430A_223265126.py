x = int(input())
for i in range(x):
    y = int(input())
    _3 = 0
    _5 = 0
    _7 = 0
    if (y == 1 or y == 2 or y == 4):
        print(-1)
        continue
    _3 = y // 3
    if (y % 3 == 1):
        _3 = (y - 7) // 3
        _7 = 1
    elif (y % 3 == 2):
        _3 = (y -5) // 3
        _5 = 1
    print(_3, _5, _7)
        