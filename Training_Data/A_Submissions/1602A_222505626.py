for _ in range(int(input())):
    s = input()
    x = min(s)
    i = s.index(x)
    print(x, s[:i] + s[i+1:])