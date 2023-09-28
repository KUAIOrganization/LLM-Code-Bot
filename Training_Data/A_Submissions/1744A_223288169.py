for _ in range(int(input())):
    a = int(input(""))
    b = input("").split()
    e = input("")
    c = {}
    for i in range(0, a):
        if b[i] not in c:
            c[b[i]] = e[i]
        else:
            if c[b[i]] != e[i]:
                print("NO")
                break
    else:
        print("YES")
