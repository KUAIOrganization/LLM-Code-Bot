k,r=map(int,input().split())
l=[]
for i in range(1,101):
    total=(i*k)-r
    total2=(i*k)
    if total%10==0 or total2%10==0:
        l.append(i)
        break
print(l[0])