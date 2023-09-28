t = int(input())


def nod(n):
    m = 0
    a = []
    n -= 1 * (n % 2 != 0)
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
            m = max(i, m)
    return a, m


for i in range(t):
    n = int(input())
    n -= 1 * (n % 2 != 0)
    print(n // 2)
    