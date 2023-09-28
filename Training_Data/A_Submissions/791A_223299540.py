a_b = input()
ab = a_b.split()
a = int(ab[0])
b = int(ab[1])
x = 0

while a <= b:
    a = a*3
    b = b*2
    x = x+1

print(x)
