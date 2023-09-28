n=int(input())
a=list(map(int,input().split()))
i=0
sta=1
re=[]
while i<n-1:
    while i<n-1:
        if a[i]<=a[i+1]:
            sta+=1
            i+=1
            re.append(sta)
        else:
            i+=1
            sta=1
            break
if re:
    print(max(re))
else:
    print(1)