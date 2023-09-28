# Input
n = int(input())
bottles = []

for _ in range(n):
    ai, bi = map(int, input().split())
    bottles.append((ai, bi))

# Count the number of bottles that can't be opened
cant_open = 0

for i in range(n):
    can_open = False
    for j in range(n):
        if i != j and bottles[i][0] == bottles[j][1]:
            can_open = True
            break
    if not can_open:
        cant_open += 1

# Output
print(cant_open)
