# Read input
string1 = input().lower()
string2 = input().lower()

# Compare the lowercase strings lexicographically
if string1 < string2:
    print("-1")
elif string1 > string2:
    print("1")
else:
    print("0")
