y = input()
x = int(y)
x += 1
y = str(x)
while y[1] == y[0] or y[2] == y[0] or y[3] == y[0] or y[1] == y[2] or y[1] == y[3] or y[2] == y[3]:
    x+=1
    y = str(x)    
print(x)