n = int(input())
for i in range(n):
    s = int(input())
    big_cuts = s//10
    medium_cuts = 0
    small_cuts = 0
    if 6 >= s >= 1:
        small_cuts += 1
    elif 7 <= s <= 8:
        medium_cuts += 1
    elif s == 9:
        big_cuts += 1
    else:
        s %= 10
        if s == 1 or s == 2:
            big_cuts -= 1
            small_cuts += 2
        elif s == 3 or s == 4:
            big_cuts -= 1
            medium_cuts += 1
            small_cuts += 1
        elif s == 5 or s == 6:
            big_cuts -= 1
            medium_cuts += 2
        elif s == 7 or s == 8:
            medium_cuts += 1
        elif s == 9:
            big_cuts += 1
    print(big_cuts*25 + medium_cuts*20 + small_cuts*15)
