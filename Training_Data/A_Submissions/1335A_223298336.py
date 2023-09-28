l=[]
for i in range(int(input())):
    n=int(input())
    if n%2==0:
        l.append((n/2)-1)
    else:
        l.append(n//2)
for i in l:
    print(int(i))