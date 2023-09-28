for _ in range(int(input())):
    a, b = map(int, input("").split())
    if a * 2 > b:
        print(-1, -1)
    else:
        print(a, a * 2)
