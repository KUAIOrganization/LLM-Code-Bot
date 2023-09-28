n,k = map(int,input().split())

c=0
s=0
rem = 240-k
for i in range(1,n+1):
    s=s+i*5
    if s<=rem:
        c+=1
    else:
        break
print(c)