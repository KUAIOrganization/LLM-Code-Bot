t=int(input())
for i in range(t):
    x,y=input().split()
    x=int(x)
    y=int(y)
    a,b=input().split()
    a=int(a)
    b=int(b)
    sum1=0
    list1=[]
    m=min(x,y)
    n=max(x,y)
    list1.append((m*b+(n-m)*a))
    list1.append((x+y)*a)
    print(min(list1))
