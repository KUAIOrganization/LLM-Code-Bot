for _ in range(int(input())):
    n, d = map(int,input().split())
    s = input()
    done = False

    for i in range(n):
        if int(s[i])>=d or done:
            print(s[i],end='')
        else:
            if not done: 
                print(d,end='')
                done = True
            print(s[i],end='')
    if not done:
        print(d,end='')      
        
    print()