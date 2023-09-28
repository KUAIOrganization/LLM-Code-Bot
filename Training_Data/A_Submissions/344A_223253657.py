a = int(input())
l = []
count = 0
for  i in range(a):
    b = int(input())
    l.append(b)
for j in range(a-1):
    if l[j] != l[j + 1]:
        count += 1
print(count + 1)
        
