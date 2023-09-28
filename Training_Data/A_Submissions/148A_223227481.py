k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
num = 0
for i in list(range(1,d+1)):
    if any(i % x == 0 for x in (k,l,m,n)):
        num += 1
print(num)