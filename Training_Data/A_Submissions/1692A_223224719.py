n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    count=0
    if(a<b):
        count+=1
    if(a<c):
        count+=1
    if(a<d):
        count+=1
    print(count)
    