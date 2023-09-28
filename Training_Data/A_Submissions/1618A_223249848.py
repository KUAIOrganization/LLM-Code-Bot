t = int(input())
for i in range(t):
    b = [int(i) for i in input().split()]
    for i in range(2,len(b)-1):
        if b[0]+b[1]+b[i] == b[-1]:
            c = i
    print(b[0],b[1],b[c])