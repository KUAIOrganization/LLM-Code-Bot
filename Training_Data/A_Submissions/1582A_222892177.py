for _ in range(int(input())):
	a,b,c=[int(i) for i in input().split()]
	x=a+2*b+3*c
	if x%2:
		print(1)
	else:
		print(0)