n, h = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

min_width = 0

for ha in a:
    min_width += 2 if ha > h else 1

print(min_width)