str1=input().split("+")
str1.sort()
for i in range(len(str1)):
    if i==len(str1)-1:
        print(str1[i])
    else:
        print(str1[i],end="+")