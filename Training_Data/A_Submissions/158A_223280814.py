participents_count, position = map(int, input().split(' '))
scores = list(map(int, input().split(' ')))

total_advanced = 0
for point in scores:
    if point >= scores[position-1] and point != 0:
        total_advanced += 1

print(total_advanced)