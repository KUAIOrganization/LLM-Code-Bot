R=lambda:map(int,input().split())
t,=R()
exec(t*"n,x=R();a=1+sum(x%2for x in R());print('YNeos'[a<2or~x&(a>n)or x>n-a%2::2]);")
					 	  	 							 		   	   		