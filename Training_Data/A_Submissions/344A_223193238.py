c=''
d=0
for i in range(int(input())):
    a=input()
    if a!=c:
        d=d+1
    c=a
print(d)