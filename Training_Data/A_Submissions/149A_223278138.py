n = int(input())
months = sorted([int(x) for x in input().split()], reverse=True)
counter = 0
total = 0
i = 0

if sum(months) < n:
    print(-1)
else:
    while i <= n:
        if total >= n:
            print(counter)
            break
        total += months[i]
        counter += 1
        i += 1
