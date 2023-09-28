for i in range(int(input())):
    number,donut=map(int,input().split(" "))
    if (number+1)**2-(4*donut)>=0:
        print('YES')
    else:
        print('NO')