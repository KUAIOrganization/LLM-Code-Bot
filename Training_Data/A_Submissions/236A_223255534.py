palabra=input()
caracteres = []

for i in range(len(palabra)):
    if palabra[i] not in caracteres:
        caracteres.append(palabra[i])
if len(caracteres)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
			 					 	 		  	  	 	