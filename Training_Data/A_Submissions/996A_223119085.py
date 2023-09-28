n = int(input())
denominations = [100, 20, 10, 5, 1]
num_bills = 0
for denom in denominations:
    num_bills += n // denom 
    n %= denom  
print(num_bills)