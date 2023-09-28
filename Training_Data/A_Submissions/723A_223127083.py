l = sorted(list(map(int, input().split())))
a = max(l)-l[1]
b = l[1]-min(l)
print(a+b)