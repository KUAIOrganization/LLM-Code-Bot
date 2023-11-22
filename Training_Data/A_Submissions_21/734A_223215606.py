n=input()
m=input()
lst=[]
for a in m:
    lst.append(a)
p=lst.count("A")
q=lst.count("D")
if p>q:
    print("Anton")
elif q>p:
    print("Danik")
else:
    print("Friendship")