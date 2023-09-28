from sys import stdin, stdout
import math

def read():
    return stdin.readline().rstrip()

def read_int():
    return int(read())

def read_map():
    return map(int, read().split())

def read_list():
    return list(read_map())

def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in args) + end)

def ok(val):
    write("YES") if val else write("NO")

INF = float('inf')
MOD = 1000000007

for _ in range(read_int()):
    n = read_int()
    ans = 0
    for _ in range(n):
        a, b = read_map()
        if a - b > 0:
            ans += 1
    write(ans)
