a=input()
z_count=0
flag=False
for i in range(len(a)-1,-1,-1):
    if a[i]=="0":
        z_count+=1
        if z_count==6:
            k=i
            flag=True
            break
if not flag:
    print("no")
else:
    if "1" in a[:k]:
        print("yes")
    else:
        print("no")
