data=[int(x) for x in input().split()]
n,m,a,b=data
results=[]
for i in range(n//m+2):
    rest=n-i*m
    if rest<=0:
        results.append(i*b)
    else:
        results.append(i*b+rest*a)
print(min(results))


