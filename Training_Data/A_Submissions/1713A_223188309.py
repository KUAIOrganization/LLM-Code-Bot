for _ in range(int(input())):
    xmin=ymin=xmax=ymax=0
    for _ in range(int(input())):
        x,y=map(int,input().split())
        xmin=min(xmin,x)
        xmax=max(xmax,x)
        ymin=min(ymin,y)
        ymax=max(ymax,y)
    print(2*((xmax-xmin)+(ymax-ymin)))