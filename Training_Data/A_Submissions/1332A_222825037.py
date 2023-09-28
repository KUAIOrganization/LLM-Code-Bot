for i in range(int(input())):
    ao,b,c,d=map(int,input().split())
    x,y,x1,y1,x2,y2=map(int,input().split())
    print(["Yes","No"][(x1==x2 and ao+b>0) or (y1==y2 and c+d>0) or not (x1<=x+b-ao<=x2 and y1<=y+d-c<=y2)])