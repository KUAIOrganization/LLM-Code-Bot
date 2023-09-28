z=input()
y=z.split()
i=0
k=input()
p=k.split()
i=0
s=0
while i<int(y[0]):
    if((int(p[i]))>=int(p[int(y[1])-1]) and (int(p[i]))>0):
        s=s+1
    else:
        break
    i=i+1
print(s)




