import sys
inp = sys.stdin.readline

def dubstep(n):
    parts = [part for part in n.split('WUB') if part]
    ans = " ".join(parts)
    return ans

def main():
    n = inp().strip()
    result = dubstep(n)
    print(result)

if __name__ == "__main__":
    main()