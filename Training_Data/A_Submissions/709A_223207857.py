u = list(map(int,input().split()))
m = list(map(int,input().split()))

x = 0 
y = 0 
sum = 0 
for i in range(u[0]):
    if u[1] >= m[i]:
        x = m[i]
        y += x 
    if y > u[2]:
        sum += 1
        y = 0

    x = 0 
print(sum)