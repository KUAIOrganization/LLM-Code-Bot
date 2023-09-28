x,y=input().split()
x=int(x)
y=int(y)
c=0
if y>x*x:
	print(c)
else:
	n=1
	while n<=x:
		if y%n==0:
			if y//n<=x:
				c+=1
		n+=1
	print(c)
	     
			


