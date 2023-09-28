a=str(input())
a.split(' ')
b=a.split(' ')[1]
b=int(b)
c=str(input())
c.split(' ')
e=[]
for d in c.split(' '):
    d=int(d)
    if d>=int(c.split(' ')[b-1]) and d>0:
        e.append(d)
print(len(e))
        