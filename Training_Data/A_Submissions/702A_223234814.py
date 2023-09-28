n = int(input())
nums = input().split()
nums = [int(i) for i in nums]

max = 1
actual = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        actual += 1
    else:
        if(actual > max):
            max = actual
        actual = 1

if actual > max:
    print(actual)
else:
    print(max)
