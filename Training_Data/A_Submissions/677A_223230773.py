n, h = map(int, input().split())
heights = list(map(int,input().split()))
sum = 0



for height in heights:
    if height <= h:
        sum += 1
    else:
        sum += 2

print(sum)
