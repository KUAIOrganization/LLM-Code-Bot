str_1 = input().lower()
str_2 = input().lower()
x = 0
for i in range(len(str_1)):
    if str_1[i] == str_2[i]:
        continue
    if str_1[i] > str_2[i]:
        x = 1
        break
    if str_1[i] < str_2[i]:
        x = -1
        break
print(x)