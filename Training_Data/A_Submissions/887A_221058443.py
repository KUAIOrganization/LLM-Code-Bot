a=input()
b=list(a)
m=0
for i in range(len(a)):
 if(b[i]=="1"):
    for j in range(i,len(a)):
        if(b[j]=="0"):
            m+=1
    break
if(m>=6):
    print("yes")
else:
    print("no")