x1=input().split()
n=int(x1[0])
k=int(x1[1])
l=list(map(int,input().split()))
sum=0
for x in l:
    if x>k:
        sum+=2
    else:
        sum+=1
print(sum)