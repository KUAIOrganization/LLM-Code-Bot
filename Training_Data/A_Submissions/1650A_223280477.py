
for j in range(int(input())):
    s =input()
    c =input()
    if c not in s:
        print("NO")

    else:
        assist =0
        n =len(s)
        for i in range(n):
            if s[i] == c:
                if i % 2 == 0 and (n-(i+1)) % 2 == 0:
                    print("YES")
                    assist =1
                    break

        if assist == 0:
            print("NO")                      
