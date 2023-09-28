t = int(input())
for i in range(t):
    n = int(input())
    ns = str(n)
    if len(ns) == 1 and n % 2 == 1:
        print(-1)
    elif n % 2 == 0:
        print(0)
    elif int(ns[0]) % 2 == 0:
        print(1)
    elif int(ns.count('2'))+int(ns.count('4'))+int(ns.count('6'))+int(ns.count('8')) == 0:
        print(-1)
    else:
        print(2)