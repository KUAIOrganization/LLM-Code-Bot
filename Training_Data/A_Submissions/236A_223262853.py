# Read input
username = input()

# Count the number of distinct characters
distinct_characters = set(username)

# Check if the number of distinct characters is odd
if len(distinct_characters) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
