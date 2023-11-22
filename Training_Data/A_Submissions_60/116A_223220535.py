n=input()
x,y=input().split()
p=x+y
lst=[int(p)]
for i in range(int(n)-1):
    m,n=input().split()
    p=int(p)-int(m)+int(n)
    lst.append(int(p))
max=max(lst)
print(max)