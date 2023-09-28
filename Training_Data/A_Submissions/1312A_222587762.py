import math
for _ in range(int(input())):
    m,n = map(int,input().split())
    if math.gcd(m,n) == min(m,n):
        print("YES")
    else:
        print("NO")