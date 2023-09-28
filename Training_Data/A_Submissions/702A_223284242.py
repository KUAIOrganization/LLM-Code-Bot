n = int(input())
a = list(map(int, input().split()))
conteo = 1
maximo = 1

for i in range(1, n):
    if a[i] > a[i - 1]:
        conteo += 1
    else:
        if conteo > maximo:
            maximo = conteo
        conteo = 1

if conteo > maximo:
    maximo = conteo

print(maximo)

   			 	  		 		 		 		 			 	   	