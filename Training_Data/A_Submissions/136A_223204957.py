n=int(input())
str_1=input().split()
for i in range(n):
    a=int(str_1.index(str(i + 1))) + 1
    if i!=n-1:
        print(a,end=" ")
    else:
        print(a)