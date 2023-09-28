n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
num=1
for i in range(n-1):
    if a[i]!=a[i+1]:
        num+=1
print(num)