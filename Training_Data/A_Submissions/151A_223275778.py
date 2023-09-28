# Read input values
n, k, l, c, d, p, nl, np = map(int, input().split())

# Calculate the maximum number of toasts each friend can make
toasts_drink = (k * l) // (n * nl)
toasts_lime = c * d // n
toasts_salt = p // (n * np)

# Find the minimum of the three values and print it
print(min(toasts_drink, toasts_lime, toasts_salt))
