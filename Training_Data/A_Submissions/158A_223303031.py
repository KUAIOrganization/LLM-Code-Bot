# Read input values
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Calculate the k-th place finisher's score (0-based index)
k_score = scores[k - 1]

# Count the number of participants who advance to the next round
count = 0

# Iterate through the scores and check eligibility
for score in scores:
    if score >= k_score and score > 0:
        count += 1

# Print the result
print(count)

	   	 	 	  	 	 	 				 		 	  	 	