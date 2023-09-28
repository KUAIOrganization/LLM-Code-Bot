l=list(map(int,input().split('+')))
l=sorted(l)
l=[str(i) for i in l]
c='+'
print(c.join(l))