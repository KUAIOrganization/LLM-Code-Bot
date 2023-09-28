def min_moves_to_divisible(a, b):
    remainder = a % b
    if remainder == 0:
        return 0
    return b - remainder
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = min_moves_to_divisible(a, b)
    print(result)
