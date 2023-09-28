a = int(input())
for i in range(a):
    b = int(input())
    t = str(b / 3).split('.')
    g = int(t[0])
    r = int(t[1][0])
    if r == 0:
        print(g,g)
    elif r < 5:
        print(g + 1,g)
    else:
        print(g,g + 1)