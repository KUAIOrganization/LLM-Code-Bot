N = int(input())
a, b = 0, 0
while N > 0:
    m, c = map(int, input().split())
    if m > c: a += 1;
    elif m < c: b += 1;
    N -= 1
if a > b: print("Mishka")
elif a < b: print("Chris")
else: print("Friendship is magic!^^")