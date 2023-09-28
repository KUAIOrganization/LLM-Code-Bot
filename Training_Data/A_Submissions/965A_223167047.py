k, n, s, p = map(int, input().split())
sheets = k * ((n + s - 1) // s)
packs = (sheets + p - 1) // p
print(packs)
