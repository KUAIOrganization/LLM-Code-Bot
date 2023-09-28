n=int(input())
s=input()
k=str(s)
if s.lower()==k:
    if 1<=n<=100 and n==len(s):
        l=[]
        p=[]
        g=('a','e','i','o','u','y')
        for i in (g):
            for j in g:
                l.append(i+j) 
        for u in s:
            p.append(u)          
        def func():
            for i in range(0,len(p)-1):
                for j in range(1,len(p)):
                    if j==i+1:
                        
                        y=p[i]+p[j]
                        
                        if y in l:
                            
                            p.pop(j)
                            func()
                        else:
                            pass
        func()
        for i in p:
            print(i,end='')
