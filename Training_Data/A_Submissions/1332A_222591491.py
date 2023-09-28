import sys
input = sys.stdin.readline

def readList():
    return list(map(int, input().split()))
def readInt():
    return int(input())
def readInts():
    return map(int, input().split())
def readStr():
    return input().strip()


# BF, EC, DB, CC, CL
def solve():
    a, b, c, d = readInts()
    x, y, x1, y1, x2, y2 = readInts()
    u, v = b - a, d - c
    if u == 0 and x == x1 == x2 and a:
        return "NO"
    if v == 0 and y == y1 == y2 and c:
        return "NO"
    return "YES" if x1 <= x + u <= x2 and y1 <= y + v <= y2 and x1 <= x <= x2 and y1 <= y <= y2 else "NO"


for _ in range(readInt()):
    print(solve())
