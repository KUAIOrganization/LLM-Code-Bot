x = input()
c = []
for i in x:
    if i.isdigit():
        c.append(int(i))
c.sort()
a= '+'.join(map(str,c))
print(a)
	  	   	 		 	 	 	 	 			 	   	 	