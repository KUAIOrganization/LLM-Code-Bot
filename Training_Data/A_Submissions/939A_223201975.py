def has_love_triangle(n, planes):
    for i in range(n):
        x = planes[i]
        y = planes[x - 1]  
        z = planes[y - 1]  
        if z == i + 1: 
            return "YES"
    return "NO"

n = int(input())
planes = list(map(int, input().split()))

res = has_love_triangle(n, planes)
print(res)