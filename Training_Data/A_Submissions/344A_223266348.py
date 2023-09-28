t=int(input())
n=int(input())
c=1
for _ in range(t-1):
    n1=int(input())
    if n1!=n:
        n=n1
        c=c+1
print(c)