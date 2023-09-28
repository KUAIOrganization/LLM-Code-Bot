a=[]
b=[]
c=0
for i in range(int(input())):
    p,q=map(int,input().split())
    a.append(p)
    b.append(q)
for i in range(len(a)):
    for j in range(len(a)):
        if(b[j]==a[i] and i!=j):
            c=c+1
            break
print(len(a)-c)
                