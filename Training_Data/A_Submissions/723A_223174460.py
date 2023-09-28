a,b,c=map(int,input().split())
if a>b and a>c:
    max=a
    if b>c:
        min=c
    else:
        min=b
elif b>c and b>a:
    max=b
    if a>c:
        min=c
    else:
        min=a
else:
    max=c
    if b>a:
        min=a
    else:
        min=b
print(max-min)