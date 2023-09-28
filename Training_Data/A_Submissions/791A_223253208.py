a, b = list(map(int, input().split()))
count = 0
while b >= a:
    b *= 2
    a *= 3
    count += 1
print(count)
