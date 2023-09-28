a=int(input())
b=list(map(int,input().split()))
c=sum(b)
b.sort()
d=0
e=0
for i in range(0,a):
    d+=b[a-i-1]
    if d>c/2:
        e=i+1
        break
print(e)

