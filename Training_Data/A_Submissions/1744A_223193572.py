e=int(input())
for _ in range(e):
	w=int(input())
	r=list(map(int,input().split()))
	p=input()
	res="Yes"
	for k in range(w):
		for m in range(w):
			if(r[k]==r[m] and p[k]!=p[m]):
				res="No"
	print(res)