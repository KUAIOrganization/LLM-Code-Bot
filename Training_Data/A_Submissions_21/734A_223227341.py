s=int(input())
k=input()
a=0
d=0
for i in range(0,s):
    if(k[i]=="A"):
        a+=1
    else:
        d+=1
if(a>d):
    print("Anton")
elif(d>a):
    print("Danik")
else:
    print("Friendship")
