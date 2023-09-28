n, h = map(int, input().split())
a = list(map(int, input().split()))

i = 1
j = 0
sum = 0

while i <= n:
    if a[j] <= h:
        sum+=1
    else:
        sum+=2
    j+=1
    i+=1


print(sum)