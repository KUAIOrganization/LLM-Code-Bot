n=input()
n =int(n)
x=0
for i in range(1,n+1):
    s=input()
    s=str(s)
    if s=="X++" or s=="++X":
        x+=1
    else:
        x-=1
print(x)
 	     		 	   	     	 			 				