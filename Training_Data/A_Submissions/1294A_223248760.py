n = int(input())

def can(a,b,c,n):
    m = [a,b,c]
    m.sort()
    
    minus = (m[2] - m[1]) + (m[2] - m[0])
    
    n -= minus
    
    if n < 0 or n % 3 != 0:
        return False
    else:
        return True
        
for i in range(n):
    a, b, c, m = map(int,input().split())
    
    if can(a, b, c, m):
        print("YES")
    else:
        print("NO")
    