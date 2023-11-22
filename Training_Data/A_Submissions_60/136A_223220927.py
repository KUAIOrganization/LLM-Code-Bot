n = int(input())
mas = [int(el) for el in input().split()]
ans = [0] * n
for i in range(n):
    ans[mas[i] - 1] = i + 1
print(*ans)