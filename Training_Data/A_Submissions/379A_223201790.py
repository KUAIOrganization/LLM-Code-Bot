a,b= input().split()
a=int(a)
b=int(b)
hours=0
rem=0
while((a+rem)>=b):
    t=((a+rem)//b)
    rem=(a+rem)%b
    hours+=a
    a=t
hours+=a
print(hours)