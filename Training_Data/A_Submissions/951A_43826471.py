s = input()
ans = 1
t = 1
for i in range(-len(s) + 1, len(s) - 1):
    if s[i] == s[i + 1]:
        t = 1
    else:
        t += 1
    ans = max(ans, t)
ans = min(ans, len(s))
print(ans)
