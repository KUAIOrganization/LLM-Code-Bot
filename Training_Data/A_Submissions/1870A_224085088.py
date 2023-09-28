def adapt(string):
    return [int(_) for _ in string.split(' ')]

nrow = int(input())
for _ in range(nrow):
    n, k, x = adapt(input())
    if n < k or k - x > 1:
        print(-1)
    else:
        sum = k*(k - 1)/2 + (n - k)*(x - int(k == x))
        print(round(sum))