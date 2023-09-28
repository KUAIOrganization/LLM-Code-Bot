for _ in range(int(input())):
    n=int(input())
    lst=[abs(int(x)) for x in input().split()]
    dc=0
    lst.sort()
    s=set(lst)
    for i in s:
        if(i==0):
            dc+=1
        elif(lst.count(i)>=2):
            dc+=2
        else:
            dc+=1
    print(dc)