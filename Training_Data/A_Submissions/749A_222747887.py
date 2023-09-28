x = int(input())
z = 0
c = 0
while x > 0:
  if x > 3:
    x -= 2
    z += 1
  elif x == 3:
    x -= 3
    c += 1
  else:
    x -= 2
    z += 1
print(z+c)
print('2 ' * z + '3' * c)