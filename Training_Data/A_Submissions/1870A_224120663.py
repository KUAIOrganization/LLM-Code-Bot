import math
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
def RSIL(): return sorted(map(int, input().split()), reverse=True)
from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
import copy

sys.setrecursionlimit(2500)



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
