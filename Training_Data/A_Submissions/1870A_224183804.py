t=int(input())
for i in range(t):
    n,k,x=map(int, input().split())
    if k-1>x or k>n:
        print(-1)
    else:
        h=int(k*(k-1)/2)
        f=n-k
        if x!=k:
            print(h+f*x)
        else:
            print(h+f*(x-1))
