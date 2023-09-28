t = int(input())

while(t>0):
    n , k = map(int, input().split())
    raw_list =list(map(int, input().split()))
    sub_list = [0] * (len(raw_list)-1)
    for i in range(0, len(raw_list)-1):
        sub_list[i] = abs(raw_list[i] - raw_list[i+1])



    for i in range(k-1):
            
        max_index = sub_list.index(max(sub_list))
        sub_list[max_index] = 0


    # print sum of sub_list
    print(sum(sub_list))        
            


    
    
    
    
    t -= 1
 	  			 	      	  	   		   	  	