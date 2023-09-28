t=int(input())
while t:
    t-=1
    a,b,c,d=[int(x) for x in input().split(" ")]
    x,y,x1,y1,x2,y2=[int(x) for x in input().split(" ")]
    if ((x1<=(x-a+b)<=x2) and (x1<x2 or a+b==0)) and ((y1<=(y-c+d)<=y2) and (y1<y2 or c+d==0)): print("Yes")
    else: print("No")