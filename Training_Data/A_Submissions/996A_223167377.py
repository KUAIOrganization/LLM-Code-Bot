a=int(input())
s=0
s+=a//100
a=a%100
s+=a//20
a=a%20
s+=a//10
a=a%10
s+=a//5
a=a%5
s+=a//1
a=a%1
print(s)