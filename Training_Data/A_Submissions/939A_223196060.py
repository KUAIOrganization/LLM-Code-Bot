def find_love_triangle(n, planes):
    for i in range(n):
        a = i
        b = planes[i] - 1  # Adjust for 0-based indexing
        c = planes[b] - 1  # Adjust for 0-based indexing
        
        if planes[c] - 1 == a:
            return "YES"
    
    return "NO"

# Input
n = int(input())
planes = list(map(int, input().split()))

# Output
result = find_love_triangle(n, planes)
print(result)
