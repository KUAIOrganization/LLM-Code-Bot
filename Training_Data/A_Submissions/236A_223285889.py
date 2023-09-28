str1=input()
a=0
for i in range(97,123):
    if str1.find(chr(i))!=-1:
        a+=1
if a%2==1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")