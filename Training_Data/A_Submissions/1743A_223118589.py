t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().strip().split()))[:n]
    s = 0
    c = 10 - n -1
    for i in range(1, c + 1):
        s += (i * 6)
    print(s)