n = int(input())
if n % 2 == 0:
    a = n // 2
    print(a)
    for i in range(0,a):
        print("2", end=" ")
else:
    a = n // 2
    print(a)
    for i in range(0, a):
        if i == a - 1:
            print("3", end=" ")
        else:
            print("2", end=" ")
# Tue Sep 12 2023 17:18:38 GMT+0300 (Moscow Standard Time)

# Tue Sep 12 2023 17:18:44 GMT+0300 (Moscow Standard Time)
