n=int(input())
count=0
for _ in range(n):
    occ,maxi=map(int,input().split())
    if occ<=maxi-2: count+=1
print(count)