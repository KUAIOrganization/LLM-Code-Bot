T = int(input())
for i in range(T):
    p, q, r = map(int, input().split())
    print(1 + min(p - 1, q + r) * 2)