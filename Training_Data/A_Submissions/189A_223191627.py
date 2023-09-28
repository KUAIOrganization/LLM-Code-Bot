def cut_ribbon(n, a, b, c):
    dp = [-1e5] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        if i-a >= 0: dp[i] = max(dp[i], dp[i-a] + 1)
        if i-b >= 0: dp[i] = max(dp[i], dp[i-b] + 1)
        if i-c >= 0: dp[i] = max(dp[i], dp[i-c] + 1)

    return dp[n] if dp[n] > 0 else -1

data=[int(x) for x in input().split()]
n,a,b,c=data
print(cut_ribbon(n, a, b, c))