for i in range(int(input())):
    n,k,x = map(int,input().split())
    d,i,z = [],0,n
    if k>n or k-1>x:
        print(-1)
        continue
    while i<k:
        d.append(i)
        i+=1
        z-=1
    for i in range(z):
        d.append(x-int(k==x))

    print(sum(d))
