a,b=input().split()
a=int(a)
b=int(b)
# a=7
# b=4
c=a
sum=0
while(a//b!=0):
    burnt=a%b
    sum+=a//b
    if((a//b+burnt)<b):
        break
    else:
        a=a//b+burnt
print(sum+c)
