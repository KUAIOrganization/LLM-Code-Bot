r=int(input())
for i in range(r):
    d=int(input())
    s=list(map(int,input().split()))
    w1=s[0]
    w2=s[d-1]
    w3=s[d//2]
    e=list(set(s))
    if (e[0]==w1 and e[0]==w2) or (e[0]==w2 and e[0]==w3) or (e[0]==w3 and e[0]==w1) :
        print(s.index(e[1])+1)
    else: print(s.index(e[0])+1)    