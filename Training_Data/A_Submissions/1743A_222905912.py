import math

def c(n,k):
    return (math.factorial(n))/(math.factorial(n-k)*math.factorial(k))
    
def check(n):
    m=10-n
    return c(m,2)*c(4,2)
    
t=int(input())
d=[]
for i in range(t):
    n=int(input())
    s=input().split()
    d.append(check(n))
    
for i in d:print(int(i))