# your code goes here
t=int(input())
a=list(map(int,input().split()))
m=max(a)
s=0
for i in a:
	s+=(m-i)
print(s)
