r=int(input())
c=0
for i in range(r):
    n=input().split(' ')
    if int(n[0])+2<=int(n[1]):
        c+=1
print(c)