for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    if not (a and b):
        print(0)
        continue
    if 0.5<a/b<2:
        print((a+b)//3)
    else:
        print(min(a,b))