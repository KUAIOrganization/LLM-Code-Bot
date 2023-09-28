n = int(input())
list1 = []
for i in range(n):
    a, b = map(int, input().split())

    if (a < b):
        list1.append("Chris")
    elif (a > b):
        list1.append("Mishka")
m = list1.count("Mishka")
c = list1.count("Chris")
if (m > c):
    print("Mishka")
elif (c > m):
    print("Chris")
else:
    print("Friendship is magic!^^")
