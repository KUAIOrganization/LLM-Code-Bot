for _ in[0]*int(input()):
    n,d = input().split()
    s = input()
    j = 0
    while j < len(s) and s[j] >= d:
        j += 1
    print(s[:j]+d+s[j:])