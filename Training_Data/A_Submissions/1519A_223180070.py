for _ in range(int(input())):
    r,b,d=map(int,input().split())
    q=max(r,b)//min(r,b) -1
    if(max(r,b)%min(r,b)==0):
        w=0
    else:
        w=1
    if(q+w<=d):
        print("YES")
    else:
        print("NO")