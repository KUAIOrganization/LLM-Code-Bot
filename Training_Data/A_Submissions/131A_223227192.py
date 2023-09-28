x = str(input())
upp = 0
low = 0
for i in x:
    if i.isupper():
        upp += 1
    else: 
        low += 1

if (x[0].islower() and upp == len(x)-1):
    for i in range(len(x)):
        if i == 0:
            print(x[i].upper(), end="")
        else:
            print(x[i].lower(), end="")
elif upp == len(x):
    for i in range(len(x)):
        print(x[i].lower(),end="")
else:
    print(x)