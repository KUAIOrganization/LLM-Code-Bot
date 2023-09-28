a = int(input())
for i in range (0,a) :
    n , k , x  = map(int,input().split())
    if n  < k  or k > x+1:
        print("-1")
    elif x==k :
        print(int( ((k-1)*k) / 2 +(x-1) * (n-k)))
    else :
        print(int( ((k-1)*k) / 2 +(x) * (n-k)))
        
        
