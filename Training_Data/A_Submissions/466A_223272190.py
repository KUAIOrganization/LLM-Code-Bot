n,m,a,b = map(int, input().split())
price = 0
while n>0:
    if m>n:
        price1 = b
        price2 = a*n
        price += min(price1,price2)
        n=0
    else:
        price1 = b
        price2 = a*m
        price += min(price1,price2)
        n -= m
print(price)