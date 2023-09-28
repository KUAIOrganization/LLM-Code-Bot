(n,h) = map(int,input().split())
hlist = list(map(int,input().split()))
for x in hlist:
    if x > h:
        n += 1
print(n)
