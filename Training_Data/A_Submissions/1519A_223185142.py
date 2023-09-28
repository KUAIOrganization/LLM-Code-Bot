for _ in range(int(input())):
    r,b,d=map(int,input().split())
    if(max(r,b)<=min(r,b)*(d+1)):
        print("YES")
    else:
        print("NO")