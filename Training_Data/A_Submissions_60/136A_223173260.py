a=int(input())
b=list(map(int,input().split()))
c=["0"]*a
for i in range(0,a):
    c[(b[i]-1)]=str(i+1)
print(" ".join(c))