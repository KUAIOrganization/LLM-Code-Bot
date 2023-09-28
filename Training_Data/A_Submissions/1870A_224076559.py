def solve():
    n, k, x = map(int, input().split())
    
    if x < k - 1 or n < k:
        print(-1)
        return
    
    if x == k:
        x -= 1
    
    sum_val = (n - k) * x + k * (k - 1) // 2
    print(sum_val)

t = int(input())
for _ in range(t):
    solve()
