n=int(input())
poss=[]
count=1
for _ in range(n):  poss.append(input())
for i in range(n-1):
    if poss[i]!=poss[i+1]:  count+=1
print(count)