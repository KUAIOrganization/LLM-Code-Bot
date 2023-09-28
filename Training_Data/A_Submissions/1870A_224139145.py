for i in range(int(input())):
    n,k,x = map(int,input().split())
    # print(mexanizedarray(n,k,x))
    if k-x>1:
        print (-1)
    elif k>n:
        print (-1)
    else:
        if x==k:
            x-=1

        initial=((k-1)*(k))/2
        initial+=(n-k)*x
        
        print (int(initial))