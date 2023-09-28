n=int(input())
a=[int(i) for i in input().split()]
c=max(a)
d=a.index(c)
e=d
del a[d]
a.insert(0,c)
q=min(a)
for i in range(n):
    if a[i]==q:
        k=i 
p=n-k-1
print(e+p)


