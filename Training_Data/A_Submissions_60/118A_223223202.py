a=input()
a=str(a)
v=["a","e","i","o","u","y","A","E","I","O","U","Y"]
lst=[]
for i in a:
    if (i  not in v and i.isalpha()==True):
        lst.append(".")
        lst.append(i.lower())
    else:
        pass
ans=""
for j in lst:
    ans+=j
print(ans)
    
    
