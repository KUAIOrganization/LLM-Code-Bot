net=int(input())
l=list(map(int,input().split()))
s=l.index(max(l))+l[::-1].index(min(l))
print(s-(s>=net))