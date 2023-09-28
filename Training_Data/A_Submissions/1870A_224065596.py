t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if min(n, x + 1) < k:
        print(-1)
    else:
        if k == x:
            x -= 1
        ans = k * (k - 1) // 2 + (n - k) * x
        print(ans)
