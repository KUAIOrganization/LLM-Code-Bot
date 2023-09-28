v=0
a,b=map(int,input().split())
for i in range(1,a+1):
    c=input()
    d=c.count('C')
    v=c.count('M')
    m=c.count('Y')
    if d>0 or v>0 or m>0:
        print('#Color')
        v=1
        break
if v==0:
    print('#Black&White')
