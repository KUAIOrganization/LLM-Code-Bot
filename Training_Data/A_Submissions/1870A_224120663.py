import math

import sys


def I(): return int(input())

def II(): return map(int, input().split())

def solve():

    n, k, x = II()

    total = 0

    # if (k > n and n < x) or (k > x + 1):

    #     print(-1)

    # else:

    maxi = 0

    for i in range(n):

        if i < k and i <= x:

            total += i

            maxi = max(i, maxi)

        else:

            if x == k:

                total += x - 1

            else:

                total += x

    # print(maxi)

    if maxi + 1 == k:

        print(total)

    else:

        print(-1)

T = I()
for ___ in range(T):

    solve()
