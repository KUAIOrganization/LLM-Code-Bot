n = int(input())
ca = 0
for i in range(n):
    a = [int(num) for num in input().split()]
    if (a[1] - a[0] >= 2):
        ca += 1

print(ca)