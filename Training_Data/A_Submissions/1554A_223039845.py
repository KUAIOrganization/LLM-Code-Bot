def check(d):
    n=len(d)
    prev=d[0]
    res=d[0]
    for i in range(1,n):
        prod=d[i]*prev
        if(prod>res):
            res=prod
        else:
            res=res
        prev=d[i]
    return res
    
t=int(input())
d1=[]
for i in range(t):
    d=[]
    n=int(input())
    s=input().split()
    d=list(map(int,s))
    d1.append(check(d))
    
for i in d1:print(i)