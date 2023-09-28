a=list(map(int,input().split(" ")))
n=a[0]
h=a[1]
height=list(map(int,input().split(" ")))
width=n
for i in range(n):
    if height[i]>h:
        width+=1
print(width)