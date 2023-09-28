n, c = [int(a) for a in input().split()]
nums = list(map(int, input().split()))
counter = 0

for i in range(n-1):
    if (nums[i+1] - nums[i]) > c:
        counter = 0
    else:
        counter += 1


print(counter+1)
