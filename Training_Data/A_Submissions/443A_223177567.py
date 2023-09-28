i=input()
if i[1]=='}':
    print(0)
else:
    j=''
    for jj in i:
        if jj==" ":
            pass
        else:
            j+=jj
    v=len(i)
    f=j[1:v-1:2]
    d=set(f)
    p=len(d)
    print(p)