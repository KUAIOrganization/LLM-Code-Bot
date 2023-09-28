a,b=map(int,input().split())
k=0
while a<=b:
    a*=3
    b*=2
    k+=1
print(k)