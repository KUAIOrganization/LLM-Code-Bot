def solve():
    n, t = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    bst = -2
    for i in range(n):
        if i + a[i] <= t and (bst == -2 or b[bst] < b[i]):
            bst = i
    print(bst + 1)
 
 
t = int(input())
for _ in range(t):
    solve()