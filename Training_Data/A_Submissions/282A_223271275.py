n = int(input())

nums = [input() for i in range(n)]

count = 0

for i in nums:
    if '+' in i:
        count += 1
    else:
        count -= 1

print(count)
