n=int(input())
v,h=set(),set()
for i in range(n):
    x,y=map(int,input().split())
    v.add(x)
    h.add(y)
print(min(len(v),len(h)))