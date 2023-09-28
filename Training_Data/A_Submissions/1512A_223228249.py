n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().strip().split()))
    for i in range(0,len(a)):
        if(a.count(a[i])==1):
            print(i+1)
            