count_levels = int(input())
player_X = list(map(int, input().split()))
player_Y = list(map(int,input().split()))
count_completed_levels = 0
for i in range(1, count_levels+1):
    if i in player_X[1:]:
        count_completed_levels += 1
    else:
        if i in player_Y[1:]:
            count_completed_levels += 1
        else:
            break
if count_completed_levels == count_levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
