# n, k = [int(a) for a in input().split()]
# scores = list(map(int, input().split()))
#
# x = 0
#
# for i in range(n):
#     if scores[i] >= scores[k-1] and scores[i] > 0:
#         x += 1
#
# print(x)
#
############# Task 2
#
# print("+".join(list(map(str, sorted(input().split('+'))))))

amt = int(input())
scores = list(map(int, input().split()))

output = 0
max_num = scores[0]
min_num = scores[0]

if amt != 1:
    for i in range(1, amt):
        if scores[i] > max_num:
            output += 1
            max_num = scores[i]
        elif scores[i] < min_num:
            output += 1
            min_num = scores[i]

print(output)

