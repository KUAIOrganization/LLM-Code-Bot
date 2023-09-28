n=int(input())
a=[]
num=0
for i in range(n):
    a.append(list(map(int,input().split(" "))))
    if a[i][1]-a[i][0]>=2:
        num+=1
print(num)