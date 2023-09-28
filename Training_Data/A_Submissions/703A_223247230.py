n=input()
n=int(n)

Mishka=0
Chris=0
for i in range(n):
    m,c=input().split()
    m=int(m)
    c=int(c)
    if m>c :
        Mishka=Mishka+1
    elif c>m:
        Chris=Chris+1

if  Mishka>Chris   :
    print("Mishka")
elif Chris>Mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")



	 		 	 				 	 		 	   			