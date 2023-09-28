string1 = [int(i) for i in input().split()]
n, h = string1[0], string1[1]
my_list = [int(i) for i in input().split()]
count = 0
for i in range(n):
    if my_list[i] <= h:
        count += 1
    else:
        count += 2
print(count)