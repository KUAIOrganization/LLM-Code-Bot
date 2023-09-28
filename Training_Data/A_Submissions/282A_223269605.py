n = int(input())
x = 0
for i in range(1,n+1):
    S = str(input())
    if S == "X++" or S == "++X":
        x+=1
    else:
        x-=1
print(x)
  		    	  	   		    	   	 	 		