list1=[4,44,444,7,77,777,47,74,447,474,477,774,747,744]
t=int(input())
c=1
for i in list1:
    if t%i==0:
        print("YES")
        c=0
        break
if c==1:
    print("NO")
    