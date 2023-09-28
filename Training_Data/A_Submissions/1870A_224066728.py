
t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().split()))
    if k > n or x < k-1:
        print(-1)
        continue
    # Aquí tots tenen n > k, i x >= k
    resultat = (k-1)*k//2
    if x == k:
        resultat += (k-1)*(n-k)
    else:
        resultat += x*(n-k)
    print(resultat)