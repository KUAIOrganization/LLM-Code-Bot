raw=input().split()
a=int(raw[0])
b=int(raw[1])
if a%2==0:
    if 2*b<=a:
        x=2*b-1
    else:
        x=2*(b-a//2)
else:
    if b<=(a//2)+1:
        x=2*b-1
    else:
        x=2*(b-((a//2)+1))
print(x)