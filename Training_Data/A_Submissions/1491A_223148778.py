n, t = map(int, input().split())
arr = [0] + list(map(int, input().split())) 

one = arr.count(1)
zero = arr.count(0)

for _ in range(t):
    a, b = map(int, input().split())
    if a == 1:
        if arr[b] == 1:
            arr[b] = 0
            one -= 1
            zero += 1
        else:
            arr[b] = 1
            zero -= 1
            one += 1
    elif a == 2:
        if b <= one:
            print(1)
        else:
            print(0)
