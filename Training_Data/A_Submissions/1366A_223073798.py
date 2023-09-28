n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    print(min((x+y)//3,x,y))