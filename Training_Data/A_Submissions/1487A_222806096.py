for _ in "8" *int(input()):
    n = int(input()); l = [*map(int, input().split())]; mn = sorted(l)[0]; nums = 0
    for c in l:
        if c>mn:
            nums+=1
    print(nums)
