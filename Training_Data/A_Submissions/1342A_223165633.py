for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if (x>=0 and y>=0) or (x<=0 and y<=0):
        x=abs(x)
        y=abs(y)
        mini=min(x,y)
        maxi=max(x,y)
        print(min(mini*b+(maxi-mini)*a,(x+y)*a))
    else:
        print(abs(x-y)*a)