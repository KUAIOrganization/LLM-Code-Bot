t = int(input())
for _ in range(t):
    s = input()
    k = 1
    for i in s:
        if int(i) > k:
            k = int(i)
    print(k)