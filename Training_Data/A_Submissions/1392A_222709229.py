for i in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))
    if len(a) > 1:
        print(1)
    else:
        print(n)
