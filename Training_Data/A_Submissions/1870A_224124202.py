for i in range(int(input())):
    n,k,x=map(int,input().split())
    if min(n,x+1)<k:
        print(-1)
    else:
        if k==x:
            x-=1
        print((n-k)*x+(k*(k-1))//2)
    
