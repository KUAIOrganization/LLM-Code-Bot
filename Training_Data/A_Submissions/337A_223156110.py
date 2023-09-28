n,m=map(int,input().split())
list=[int(i) for i in input().split()]
list.sort()
num=list[n-1]-list[0]
for i in range(m-n+1):
    num=min(num,list[i+n-1]-list[i])
print(num)