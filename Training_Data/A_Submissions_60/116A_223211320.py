
n = int(input())
sum = 0
list0 = []
for i in range(n):
    a,b = map(int,input().split())
    sum -= a
    sum += b
    list0.append(sum)
print(max(list0))

    

