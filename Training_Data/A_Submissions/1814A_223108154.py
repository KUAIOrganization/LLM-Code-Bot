def Coins():
    n, k = [int(num) for num in input().split()]
    if n%2==0:
        print('Yes')
    elif k%2==0 or k > n:
        print('No')
    else:
        print('Yes')

n = int(input())
for i in range(n):
    Coins()