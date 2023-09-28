c,b,a,s=map(int,input().split())
sums=max(c,b,a,s)
if abs(c-sums)!=0:
    print(abs(c-sums),end=' ')
    
if abs(a-sums)!=0:
    print(abs(a-sums),end=' ')
    
if abs(b-sums)!=0:
    print(abs(b-sums),end=' ')
    
if abs(s-sums)!=0:
    print(abs(s-sums),end=' ')
