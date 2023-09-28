a,b=map(int,input().split())
c=240-b
s=0
i=1
for i in range(a):
    c-=5*(i+1)
    if c<0:
        break
    else:
        s+=1
print(s)