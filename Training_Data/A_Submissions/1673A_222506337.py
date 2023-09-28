for i in range(int(input())):
    s=input()
    a=[]
    for i in range(len(s)):
        a.append(ord(s[i])-96)
    if len(s)%2==0:
        print('Alice', sum(a))
    elif len(s)==1:
        print('Bob', sum(a))
    else:
        print('Alice', max(sum(a)-a[len(a)-1]*2, sum(a)-a[0]*2))