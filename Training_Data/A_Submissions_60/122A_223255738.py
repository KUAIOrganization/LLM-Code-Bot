n = int(input())
if 1000 >= n >= 1:
    l = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
    flag = False
    for i in l:
        if n % i == 0:
            flag = True
            break
        else:
            continue
    if flag:
        print('YES')
    else:
        print('NO')
