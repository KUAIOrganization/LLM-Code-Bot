
n,*a=map(int,open(0).read().split())
b=a.index(max(a))+a[::-1].index(min(a))
print(b-(b>=n))
