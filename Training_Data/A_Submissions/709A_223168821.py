n,b,d=map(int,input().split())
l=list(map(int,input().split()))
s=0
a=0
for x in l:
	if x<=b:
		s+=x
	if s>d:
		s=0
		a+=1
print(a)