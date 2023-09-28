n = int(input())
a = list(map(int, input().split()))

sum = 0

a.sort()
for i in range(n):
    sum += a[i]

if sum % 2 != 0:
    i = 0
    while True:
        if a[i] % 2 != 0:
            sum -= a[i]
            break
        i += 1

print(sum)