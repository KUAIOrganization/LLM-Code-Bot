
t = int(input())

for _ in range(t):
    n = int(input())
    
    
    if n % 2 == 0:
        max_gcd = n // 2
    else:
        max_gcd = (n - 1) // 2
    
    print(max_gcd)
