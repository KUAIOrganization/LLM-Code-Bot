operations, ice_creams = map(int, input().split())
sad = 0

for i in range(operations):
    h, num = input().split()
    num = int(num)
    if h == '+':
        ice_creams += num
    if h == '-':
        if num <= ice_creams:
            ice_creams -= num
        else:
            sad += 1

print(ice_creams, sad)

