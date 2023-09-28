t=int(input())
def timecount(a,b,c,d):
    if b>=a:
        return b
    elif d>=c:
        return -1
    else:
        s=b
        time=b
        if (a-b)%(c-d)==0:
            n=(a-b)//(c-d)
        else:
            n=(a-b)//(c-d)+1
        time=c*n+b
        return time
for i in range(1,t+1):
    a,b,c,d=map(int,input().split())
    print(timecount(a,b,c,d))    