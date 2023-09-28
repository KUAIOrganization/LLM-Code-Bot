y= int(input())
 
for i in range(y):
    n = int(input())
    nums = list(map(int, input().split()))
 
    max_n1 = 0
    max_n2 = 0
 
    for i in range(n):
        num = nums[i]
        if num >= max_n1:
            max_n2 = max_n1
            max_n1 = num
 
        elif num > max_n2:
            max_n2 = num
 
    print(max_n2 + max_n1) 