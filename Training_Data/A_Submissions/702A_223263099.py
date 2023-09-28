def subarray(n):
    arr = []
    input_str = input()
    input_list = input_str.split()
    
    for num_str in input_list:
        e = int(num_str)
        arr.append(e)

    max_len = 1
    current_len = 1

    for j in range(1, len(arr)):
        if arr[j] > arr[j - 1]:
            current_len += 1
        else:
            current_len = 1

        max_len = max(max_len, current_len)

    print(max_len)

n = int(input())
subarray(n)

 				 			 		 		  	 					 	  	