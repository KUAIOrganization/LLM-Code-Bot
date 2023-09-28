t= int(input())
lstx=[]
lsty=[]
lsta=[]
lstb=[]
for i in range(t):
    x,y=map(int, input().split())
    a,b=map(int, input().split())
    lstx.append(x)
    lsty.append(y)
    lsta.append(a)
    lstb.append(b)
for i in range(t):
    x=lstx[i]
    y=lsty[i]
    a=lsta[i]
    b=lstb[i]
    d=0
    while(x!=0 or y!=0):
        if (x>0 and y>0):
            d+=min(2*a,b)*min(x,y)
            m=min(x,y)
            x=x-m
            y=y-m
        elif(x>0 and y<0):
            d+=a*x
            x=0
        elif(x<0 and y>0):
            d+=a*(-x)
            x=0
        elif(x<0 and y<0):
            d+=min(2*a,b)*min(-x,-y)
            m=min(-x,-y)
            x=x+m
            y=y+m
        elif(x==0 and y<0):
            d+=a*(-y)
            y=0
        elif(x==0 and y>0):
            d+=a*y
            y=0
        elif(x>0 and y==0):
            d+=a*x
            x=0
        elif(x<0 and y==0):
            d+=a*(-x)
            x=0
    print(d)

        
        
