from sys import stdin

def solve():
    a = int(stdin.readline())

    planes = list(map(int, stdin.readline().split()))

    for i in range(a):
        b = i + 1
        c = planes[i]
        d = planes[c - 1]

        if planes[d - 1] == b:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    solve()