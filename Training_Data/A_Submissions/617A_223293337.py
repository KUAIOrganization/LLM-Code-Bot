n=int(input())
x=0
for i in range(10000000):
    if n==0:
        break
    if n<2:
        n-=1
        x+=1
        break
    elif n<3:
        n-=2
        x += 1
        break
    elif n<4:
        n-=3
        x += 1
        break
    elif n < 5:
        n-= 4
        x += 1
        break
    elif n >= 5:
        n -= 5
        x += 1
print(x)