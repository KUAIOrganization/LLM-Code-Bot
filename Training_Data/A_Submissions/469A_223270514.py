def fed():
    x=int(input())
    w=input().split(' ')[1:]
    v=input().split(' ')[1:]
    for i in range(x):
        if str(i+1) not in w and str(i+1) not in v:
            return "Oh, my keyboard!"
    return "I become the guy."
print(fed())