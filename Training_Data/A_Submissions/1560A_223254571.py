
for i in range(int(input())):
    l=[]
    k=int(input())
    i=1
    while len(l)!=k:
        if i%3!=0 and str(i)[-1]!="3":
            l.append(i)
        i+=1
    for i in l:
        if str(i)[-1]==3:
            l.remove(i)

    print(l[k-1])
        