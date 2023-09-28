n = int(input())
levels = set()

for _ in range(2):
    levels.update(input().split()[1:])

if len(levels) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
