# Read input values
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Calculate the score threshold for advancement
k_score = scores[k - 1]

# Initialize a counter for participants who advance
count = 0

# Count participants who scored equal to or greater than k_score
for score in scores:
    if score >= k_score and score > 0:
        count += 1

# Print the result
print(count);
	  	  		    	 						 			 	 				