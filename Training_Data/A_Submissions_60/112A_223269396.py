first = input()
sec = input()

str1 = first.lower()
str2 = sec.lower()

if str1 < str2:
    print("-1")
elif str1 > str2:
    print("1")
else:
    print("0")