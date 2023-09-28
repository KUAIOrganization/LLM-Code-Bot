n,m=map(int, input().split())
if(m%n!=0):
    print(-1)
else:
    t=m//n
    a=0
    while(t%2==0):
        t=t//2
        a+=1
    while(t%3==0):
        t=t//3
        a+=1
    if t==1:
        print(a)
    else:
        print(-1)
        
        
    
