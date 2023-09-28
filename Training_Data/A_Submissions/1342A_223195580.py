t=int(input())
for _ in range(t):
    x,y=input().split()
    x=int(x)
    y=int(y)
    a,b=input().split()
    a=int(a)
    b=int(b)
    ans=0
    ans1=0
    maxx=0
    t=abs(x-y)
    ans=t*a
    ans1=t*a
    if x>y:
        x-=t
    else:
        y-=t
    ans+=x*b
    ans1+=x*2*a
    maxx=min(ans,ans1)
    print(maxx)
