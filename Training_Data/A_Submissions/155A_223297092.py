n=int(input())
s=list(map(int,input().split()))
big,small=s[0],s[0]
counter=0
for i in range(1,len(s)):
    if s[i]>big:
        counter+=1
        big=s[i]
    elif s[i]<small:
        counter+=1
        small=s[i]
print(counter)