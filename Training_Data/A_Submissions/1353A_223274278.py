n=int(input())

for i in range(n):
    t=[int(i) for i in input().split()]
    k=t[0]
    m=t[1]
    if k==1:
        print(0)
    elif k==2:
        print(m)
    else:
        print(2*m)
    