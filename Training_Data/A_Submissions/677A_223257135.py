n, h = map(int, input().split())
a = input().split()
a = [int(x) for x in a]
summ = 0
for i in a:
    if i > h:
        summ += 2
    else:
        summ += 1

print(summ)