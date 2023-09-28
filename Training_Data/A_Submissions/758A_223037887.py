n = int(input())
wealth = list(map(int, input().split()))
total_wealth = sum(wealth)
max_wealth = max(wealth)
min_burles = n * max_wealth - total_wealth
print(min_burles)
