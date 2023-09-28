t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    li = list(map(int, input().strip().split()))
    d = max(li)
    if d == 1:
        print('YES')
    else:
        print('NO')