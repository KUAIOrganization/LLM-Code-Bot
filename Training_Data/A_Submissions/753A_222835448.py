n = int(input())
x = int(((8*n+1)**0.5 - 1)//2) 
m = [i for i in range(1, x+1)]
m[-1] += n - x*(x+1)//2
print(x)
print(*m)