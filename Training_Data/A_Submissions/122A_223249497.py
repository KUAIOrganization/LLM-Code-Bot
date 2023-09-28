n=int(input())
lst=['4','7']
lst1=[]
lst2=[]
for i in range(n+1):
    i=str(i)
    k=1
    for j in i :
        if j not in lst:
            k=0
            break
        else:
            pass
    if k==1:
        lst1.append(i)
for i in lst1:
    lst2.append(int(i))
k=0
for l in lst2:
    if (n%l==0):
        k=1
    else:
        pass
if k==1:
    print("YES")
else:
    print("NO")
        
            
