n=int(input())
x=0
for _ in range(n):
    value=input()
    if value=="X++" or value=="++X":
        x+=1
    else:
        x-=1
print(x)
        