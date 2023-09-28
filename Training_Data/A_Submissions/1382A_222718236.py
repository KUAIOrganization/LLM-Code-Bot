for _ in "*" * int(input()):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for c in a:
        if c in b:
            print("YES")
            print(1, c)
            break
    else:
        print("NO")
