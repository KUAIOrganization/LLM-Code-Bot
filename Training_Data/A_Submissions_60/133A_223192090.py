n=input()
#print(n)
b={"H","Q","9"}
c=False
for i in n:
    if i in b:
        c=True
        break
if c:
    print("YES")
else:
    print("NO")