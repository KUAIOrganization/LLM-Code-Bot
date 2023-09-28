n, k = map(int, input().split())
num_odd = (n + 1) // 2
num_even = n // 2
if k <= num_odd:
    result = 2 * k - 1
else:
    result = 2 * (k - num_odd)
print(result)