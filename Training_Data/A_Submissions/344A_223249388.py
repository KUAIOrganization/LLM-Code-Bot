n = int(input())
mylist = [list(input()) for i in range(n)]
count = 1
res = mylist[0][0]
for i in range(len(mylist)):
    if res == mylist[i][0]:
        continue
    else:
        res = mylist[i][0]
        count += 1
print(count)