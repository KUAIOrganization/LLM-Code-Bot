def love_triangle(n, p):
    for i in range(n):
        a = i + 1
        b = p[a]  
        c = p[b]  
        if p[c] == a: 
            return "YES"  
    return "NO"  


n = int(input())
p = [0] + list(map(int, input().split()))  


result = love_triangle(n, p)
print(result)
