def solve():
    n, m, k = map(int, input().split())
    x = (k - 1) >> 1
    
    print(x // m + 1, x % m + 1, "RL"[k & 1])
    
    
if __name__ == "__main__":
    solve()
    