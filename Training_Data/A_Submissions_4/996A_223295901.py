n = int(input())
count = 0
bill_denominations = [100, 20, 10, 5, 1]
for denomination in bill_denominations:
    num_bills = n // denomination
    count += num_bills
    n -= num_bills * denomination
print(count)
