input()
l=list(map(int,input().split()))
s=[0,0]
t=0
while l:
    s[t]+=l.pop([-1,0][l[0]>l[-1]])
    t=1-t
print(*s) 