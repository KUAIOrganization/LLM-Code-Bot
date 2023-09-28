import sys

for _ in range(int(input())):
    a = int(input(""))
    b = [int(i)for i in sys.stdin.readline().split()]
    c = set(b)
    d = 0
    for i in c:
        r = b.count(i)
        d += min(r // 2 * i + r % 2, r)
    print(d)
