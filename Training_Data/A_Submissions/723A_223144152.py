x1, x2, x3 = map(int, input().split())

d1 = (x1 - x2) if x1>x2 else (x2 - x1)
d2 = (x3 - x2) if x3>x2 else (x2 - x3)
d3 = (x1 - x3) if x1>x3 else (x3 - x1)


max_num = max(d1, d2, d3)

print(max_num)