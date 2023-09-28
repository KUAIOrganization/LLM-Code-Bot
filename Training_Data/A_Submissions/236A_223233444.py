#https://codeforces.com/problemset/problem/236/A

name = str(input())
name = set(name)
x = 0
for i in name:
    x += 1

x = x%2

if x == 0:
    print("CHAT WITH HER!") # famale = even
else:
    print("IGNORE HIM!")    # male   = odd
