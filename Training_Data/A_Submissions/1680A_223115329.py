e=int(input())
for j in range(e):
	p,q,r,s=map(int,input().split())
	if p<=r<=q or r<=p<=s:
		print(max(p,r))
	else:
		print(p+r)