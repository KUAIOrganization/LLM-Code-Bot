t=int(input())
ans=[0]*t
for i in range(t):
    a,b=map(int,input().split())
    l=[]
    coun=0
    od=0
    ev=0
    l=list(map(int,input().split()))
    for j in range(a):
        if(l[j]%2==0):
            ev+=1
        else:
            od+=1
    if od%2==1 or od==0:
        t1=od
    else:
        t1=od-1
    if t1>b:
        if b%2==1 or b==0:
           t1=b
        else:
           t1=b-1
        
    t2=b-t1
    if t2<=ev and t1!=0:
        ans[i]=1
    else:
        ans[i]=0
for i in range(t):
    if(ans[i]==1):
        print("YES")
    else:
        print("NO")
	  	    					 	 	   			  		 		