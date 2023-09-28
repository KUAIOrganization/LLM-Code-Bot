
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
arr=set()
for i in range(1,d+1):
    if i%k ==0 or i%l==0 or i%m ==0 or i%n ==0:
        if i not in arr:
            arr.add(i)
print(len(arr))