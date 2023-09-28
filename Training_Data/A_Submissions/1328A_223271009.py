x=int(input())
for i in range(x):
    w,v=map(int,input().split(' '))
    if w-w//v*v==0:print(0)
    else:print(v-(w-w//v*v))