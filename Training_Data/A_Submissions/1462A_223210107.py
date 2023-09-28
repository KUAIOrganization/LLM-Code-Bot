t=int(input())
for i in range(t):
    n=int(input())
    a=[0]*n
    left=0
    right=n-1
    arr=list(map(int,input().split()))
    for i in range(n):
        if i%2==0:
            a[i]=arr[left]
            left+=1
        else:
            a[i]=arr[right]
            right-=1
    print(" ".join(map(str,a)))