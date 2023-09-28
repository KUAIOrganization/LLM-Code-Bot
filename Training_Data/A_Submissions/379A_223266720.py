a,b=map(int,input().split())
x=a
l=[]

while(b <= a and b!=0):
        k = a//b;
        z = a % b ;
        x+=k;
        a=k +z;


print(x)



'''while(a//b!=0):
    x+=a//b
    l.append(a%b)
    a=a//b
    if a//b==0:
        l.append(a%b)'''
