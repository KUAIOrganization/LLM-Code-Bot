t = input()
t = int(t)

for _ in range(t):
    n = input()
    n = int(n)
    mylist = list(map(int , input().split()))
    b_arr = []
    target = n + 1

    for i in range(n):
        b_arr.append(target - mylist[i])

    print(*b_arr)