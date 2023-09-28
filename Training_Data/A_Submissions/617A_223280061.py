n = int(input())
x = 0
step = 0
while x!=n:
    if n-x >= 5:
        x+=5
    elif n-x >= 4:
        x+=4
    elif n-x >= 3:
        x+=3
    elif n-x >= 2:
        x+=2
    elif n-x >= 1:
        x+=1
    step+=1
print(step)