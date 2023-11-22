n = int(input())
def isprime(x):
    for i in range(2,int((x ** 0.5))+1):
        if x % i == 0:
            return False
    return True
if n % 2 == 0:
    print(n//2)
    print((n-2)//2 *'2 '+'2')
else:
    print((n-1)//2)
    print((n-3)//2 *'2 '+'3')
    