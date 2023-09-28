n = int(input())
for i in range(n):
    q = int(input())
    sq = [int(i) for i in input().split()]
    a = len(sq) // 2
    c = 0
    while a !=0:
        c += max(sq) - min(sq)
        sq.remove(max(sq))
        sq.remove(min(sq))
        a -= 1
    print(c)
