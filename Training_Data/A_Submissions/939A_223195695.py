def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    flag = 0
    for i in range(n):
        if a[a[a[i]-1]-1]-1 == i:
            flag = 1
            break
    
    if flag == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
