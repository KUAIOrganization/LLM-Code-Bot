a = int(input())
if a % 2 == 0:
    print(a//2)
    for i in range(a//2):
        print(2,end=" ")
else:
    b = a - 3
    print(b//2+1)
    for i_i in range(b//2):
        print(2, end=" ")
    print(3)

# Tue Sep 12 2023 12:38:13 GMT+0300 (Moscow Standard Time)
