n, m, k = map(int, input().split())

row = (k - 1) // (2 * m) + 1
column = ((k - 1) // 2) % m + 1
side = "R" if k % 2 ==0 else "L"

print(row, column, side)