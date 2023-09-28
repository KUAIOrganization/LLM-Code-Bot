n,m = map(int,input().split())
x = list(map(int,input().split()));x.sort()
pairs=[]
for i in range(m+1-n):
    diff = x[i+n-1]-x[i]
    pairs.append(diff)
print(min(pairs))