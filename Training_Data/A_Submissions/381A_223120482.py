n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in range(n):
	b=max(a[0],a[-1])
	if i%2==0:
		s+=b
	else:
		d+=b	
	a.remove(b)
print(s,d)