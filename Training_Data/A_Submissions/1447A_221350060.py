def solve():
    n = int(input())
    
    print(n)
    print(*range(1, n + 1))
    
    
if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        