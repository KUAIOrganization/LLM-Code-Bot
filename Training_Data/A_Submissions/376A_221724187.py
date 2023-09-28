s=input()
x=s.index("^")
b=a=0
for j in range(len(s)):
	if s[j]!="=" and s[j]!="^":
		if j<x:
			b+=int(s[j])*(x-j)
		else:
			a+=int(s[j])*(j-x)
if a==b:
	print("balance")
elif a>b:
	print("right")
else:
	print("left")