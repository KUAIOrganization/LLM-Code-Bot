t = int(input())
for x in range(t):
    s = input()
    ans = 0
    c = len(s)
    for i in range(c):
        count = 0
        if s[i] == '0':
            continue
        for j in range(i + 1, c):
            if s[j] == '0':
                count += 1
            else:
                ans += count
                break
    print(ans)
