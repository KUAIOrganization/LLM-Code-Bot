n,k=map(int,input().split())
while n*(n+1)//2*5>240-k:n-=1
print(n)
