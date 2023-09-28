for _ in range(int(input())):
	n,k,x = map(int,input().split())
	if x<k-1 or n<k:
		ans = -1
	else:
		if x>k:
			ans = (k-1)*(k)/2 + (n-k)*x
		else:
			ans = (k-1)*(k)/2 + (n-k)*(k-1)

	print(round(ans))