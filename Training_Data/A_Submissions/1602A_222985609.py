for i in range(int(input())):
    str = list(input())
    p = sorted(str)[0]
    str.remove(p)
    print(f"{p} {''.join(str)}")