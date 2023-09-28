tt=int(input())
for i in range(1,tt+1):
     number=input()
     x,y,n=map(int,number.split())
     k=n-((n-y)%x)
     print(k)



   	 		   	 				 	  	  		 			 	