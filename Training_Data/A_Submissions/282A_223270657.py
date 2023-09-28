n=int(input())
X=0
for i in range (1,n+1):
    s=input()
    s=str(s)
    if s=="X++" or s=="++X":
        X+=1
    else:
        X-=1
print(X)
				 		 	 	     	 		   	 	 	 	