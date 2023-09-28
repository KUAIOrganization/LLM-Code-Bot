t = int(input())
for z in range(t):
    n,k,x = list(map(int, input().split()))
    s = 0
    if min(n,x+1)<k :
        print("-1")
    
    elif k == x :
        b = n-k
        if b>0:
            s += int(k*(k-1)/2) + b*(k-1)
        elif b == 0 or b == -1 :
            s += int(k*(k-1)/2)
        elif b<0:
            s = -1
        print(s)
 
    elif k !=x :
        b = n-k
        if b>0:
            s += int(k*(k-1)/2) + b*x
        elif b == 0 or b == -1 :
            s += int(k*(k-1)/2)
        print(s)