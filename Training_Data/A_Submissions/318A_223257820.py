from math import ceil

n,k = map(int,input().split())

if k <= ceil(n/2):
    print(2*(k)-1)
else:
    print((k-ceil(n/2))*2)