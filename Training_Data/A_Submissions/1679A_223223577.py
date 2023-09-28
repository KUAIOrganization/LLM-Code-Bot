def solve():
    n = int(input())
    
    if n & 1 or n < 4:
        print(-1)
    else:
        print((n + 4) // 6, n // 4)
    
    
if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        