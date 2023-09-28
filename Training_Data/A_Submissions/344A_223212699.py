n = int(input())
nums = []
count = 1
for i in range(n):
    a = input()
    nums.append(a)
    if nums[i] != nums[i - 1]:
        count += 1
print(count)