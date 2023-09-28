for _ in range(int(input())):
    n,m,o=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    if max(l1)==n:
        print("YES")
    else:
        print("NO")