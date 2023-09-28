n = int(input())
arr = list(map(int, input().split()))

max_len = 1
cur_len = 1

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)

print(max_len)
	   	  	  	 	     	  				 	  	