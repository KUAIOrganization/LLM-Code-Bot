n=int(input())
ps=[int(x) for x in input().split()]
result=[0]*n
for i in range(n):
    result[ps[i]-1]=i+1
for j in range(n-1):
    print(str(result[j])+" ",end="")
print(str(result[n-1]))