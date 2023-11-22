n = int(input())
#n = 6
ans = ""

ans = ((n - 2) // 2) * "2 "

if n % 2:
    ans += "3"
else:
    ans += "2"
print(n//2)
print(ans)