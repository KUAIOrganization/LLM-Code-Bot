s0=input().split()
s=input().split()
n,h=int(s0[0]),int(s0[1])
w=0
for i in range(n):
    if int(s[i])<=h:
        w+=1
    else:
        w+=2
print(w)