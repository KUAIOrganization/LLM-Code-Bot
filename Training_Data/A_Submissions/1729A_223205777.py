
n=int(input())

for l in range(n):
 x=input().split()
 y= [int(i) for i in x]
 a,b,c=y[0],y[1],y[2]
 z=abs(b-c)+c-1
 if (a-1)==z : 
  print(3)
  
 elif (a-1)<z :
     print(1)
 else:
     print(2)
     
 