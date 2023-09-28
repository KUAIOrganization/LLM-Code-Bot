t = int(input())
for i in range(t):
    n, h, m = map(int, input().split())
    m1 = h * 60 + m
    mm = 1500
    for g in range(n):
        hb, mb = map(int, input().split())
        mb = hb * 60 + mb
        if mb - m1 < 0:
            mb += 1440
        if mb - m1 < mm:
            mm = mb - m1
    print(mm // 60, mm % 60)