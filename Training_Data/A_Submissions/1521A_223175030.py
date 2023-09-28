t=int(input())
l=[[0 for i in range(3)]for j in range(t)]
ans=[0]*t
for i in range(t):
    a,b=map(int,input().split())
    if(a==0 or b==0 or b==1):
        ans[i]=0
    else:
        ind=1
        a1=a*b
        count=0;
        while(count==0):
            temp=b*ind
            for j in range(1,temp+1):
                a2=a*j
                a3=a1-a2
                if a3!=0 and a3%a==0 and a2!=a3:
                    l[i][0]=a2
                    l[i][1]=a3
                    l[i][2]=a1
                    ans[i]=1
                    count+=1
                    break
                if(a3==0) or a2==a3:
                    ind+=1
                    a1=a*b*ind
                    
            if count>0:
                    break
            ind+=1
            a1=a*b*ind
for i in range(t):
    if(ans[i]==1):
        print("YES")
        print(' '.join(map(str,l[i])))
    else:
        print("NO")
    
        
        
						   		 	 	  	   			   	