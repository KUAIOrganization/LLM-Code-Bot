n = int(input())
my_list = [[int(j) for j in input().split()] for _ in range(n)]
count1 = 0
count = 0
res1 = 0
res = 0
for i in range(0, n):
    if i == 0:
        count = my_list[i][1]
        res = count - my_list[i][0]
    else:
        res = res - my_list[i][0]
        res = res + my_list[i][1]
        if count < res:
            count = res
print(count)