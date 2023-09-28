n = int(input())
i = 1
d = 0
d_list = []

while i<=n:
    a, b = map(int, input().split())
    d = d - a + b
    d_list.append(d)
    i+=1

d = max(d_list)
print(d)