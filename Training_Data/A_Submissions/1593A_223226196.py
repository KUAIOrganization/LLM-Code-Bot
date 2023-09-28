for _ in range(int(input())):
    a,b,c=map(int,input().split())
    m=max(a,b,c)
    if(a==b==c):
        print(1,1,1)
    elif(a==b and m==a):
        print(1,1,m-c+1)
    elif(a==b and m==c):
        print(m-a+1,m-b+1,0)
    elif(b==c and m==b):
        print(m-a+1,1,1)
    elif(b==c and m==a):
        print(0,m-b+1,m-c+1)
    elif(c==a and m==c):
        print(1,m-b+1,1)
    elif(a==c and m==b):
        print(m-a+1,0,m-c+1)
    else:
        if(a==m):
            a=0
        else:
            a=m-a+1
        if(b==m):
            b=0
        else:
            b=m-b+1
        if(c==m):
            c=0
        else:
            c=m-c+1
        print(a,b,c)