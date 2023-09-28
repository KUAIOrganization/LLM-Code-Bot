a,b=map(int,input().split())
r=240-b
c=0
time=0
for i in range(1,a+1):
    time+=i*5
    if time <= r:
        c+=1
print(c)