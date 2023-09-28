s = input()
usernames = {x for x in s}
n = len(usernames)

if n % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")