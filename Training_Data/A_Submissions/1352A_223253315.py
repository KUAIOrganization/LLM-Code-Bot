n=int(input())
for i in range(n):
    x=int(input())
    cnt=0
    lst=[]
    rount_cnt=0
    while x!=0:
        rem=x%10
        if rem !=0:
            lst.append(rem*(10**cnt))
            rount_cnt+=1
        cnt+=1
        x=x//10
    print(rount_cnt)
    for i in lst:
        print(i,end=" ")
    print()