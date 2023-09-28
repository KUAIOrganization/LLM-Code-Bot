def good(n,m):
    x=n*m
    b=(x//2)+1
    w=x-b
    s=""
    s1=""
    s2=""
    l=[]
    while len(s)<m:
        if(m-len(s)==1):
            s+="B"
            b-=1
        else:
            s+="BW"
            w-=1
            b-=1
    s1=s
    while w>0:
        for i in range(m):
            if w==0:
                break
            if s1[i]=="W":
                s+="B"
                s2+="B"
                b-=1
            else:
                s+="W"
                s2+="W"
                w-=1
                if w==0:
                    break
        s1=s2
        s2=""
    s+=(b*"B")
    i=0
    while i<len(s):
        l.append((s[i:(i+m)]))
        i+=m
    return l




t=int(input())
l=[]
for i in range(t):
    n,m=map(int,input().split())
    l.append(good(n,m))
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
