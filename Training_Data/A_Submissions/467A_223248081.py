n = int(input())
mylist = [[int(i) for i in input().split()] for j in range(n)]
count = 0
for i in range(n):
    if mylist[i][1] - mylist[i][0] >= 2:
        count += 1
print(count)