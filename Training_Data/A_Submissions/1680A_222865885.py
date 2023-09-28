def sol(l1, r1, l2, r2):
    if l1 <= r2 and l2 <= r1:
        return max(l1, l2)
    return l1 + l2

t = int(input().strip())
for tt in range(t):
    seq = tuple(map(int, input().strip().split()))
    print(sol(*seq))