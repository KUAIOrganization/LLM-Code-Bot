n = input()
n = int(n)

mishka = 0
chris = 0
for i in range(n):
    m, c = input().split()
    m = int(m)
    c = int(c)
    if m > c:
        mishka = mishka + 1
    elif c > m:
        chris = chris + 1

if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
	   	  	  	 					 	 		  	  		