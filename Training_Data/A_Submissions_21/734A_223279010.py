m = int(input())
x = input()
az = 0
dz = 0
n = 0
while(n < m):
    if x[n] == 'A':
        az += 1
    else:
        dz += 1
    n += 1
if az == dz:
    print("Friendship")
elif az > dz:
    print("Anton")
else:
    print("Danik")