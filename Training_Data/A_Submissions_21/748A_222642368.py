n, m, k  = map(int, input().split())
pos = 'L'
if k & 1 == 0: pos = 'R'
k = (k >> 1) + (k & 1)
print((k - 1) // m + 1, end = " ")
if k % m == 0: print(m, pos)
else: print(k % m, pos)