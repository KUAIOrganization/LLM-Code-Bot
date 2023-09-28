z = []
z[0:] = map(int, input().split())
lst = []
if (z[0] == z[2] and z[1] != z[3]) or (z[0] != z[2] and z[1] == z[3]) :
    lst.append(1)
elif z[0] == z[2] and z[1] == z[3]:
    lst.append(0)
else:
    lst.append(2)
if (z[0] + z[2]) % 2 != (z[1] + z[3]) % 2:
    lst.append(0)
elif abs(z[0] - z[2]) == abs(z[1] - z[3]):
    lst.append(1)
else:
    lst.append(2)
lst.append(max(abs(z[0] - z[2]),abs(z[1]-z[3])))

for i in range(3):
    print(lst[i] , end= " ")