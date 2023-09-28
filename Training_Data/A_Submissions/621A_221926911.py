n = int(input())
a = [int(i) for i in input().split()]
odd = []
even = []
for it in a:
    if (it % 2) == 0:
        even.append(it)
    else:
        odd.append(it)
ans = sum(even)
if (len(odd) % 2) == 1:    
    odd.sort()
    odd.pop(0)
ans += sum(odd)
print(ans)

 		 		  					  	  		 		  			