l=[]
for i in range(int(input())):
    n=[j for j in input()]
    n.reverse()
    l2=[]
    for i in range(len(n)):
        if n[i]=="0":
            continue
        else:
            l2.append(n[i]+("0"*i))
    l2.reverse()
    l.append(l2)
for i in l:
    print(len(i))
    a=''
    for j in i:
        a+=j+' '
    print(a)