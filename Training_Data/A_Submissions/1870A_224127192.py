testCase = int(input())
for i in range(testCase):
    n, k, x = map(int, input().split())
    if min(n, x + 1) < k:
        print(-1)
    else:
        if x == k:
            sum = ((k * (k - 1)) // 2) + (n - k) * (k - 1)
            print(sum)
        else:
            sum = ((k * (k - 1)) // 2) + (n - k) * x
            print(sum)
