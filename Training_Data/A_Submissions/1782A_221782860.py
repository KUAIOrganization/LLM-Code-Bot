p = int(input())
for _ in range(p):
    pr,d,h = map(int, input().split())
    a,b,f,g= map(int, input().split())
    print(2*min(a,pr-a,b,d-b,f,pr-f,g,d-g)+abs(a-f)+abs(b-g)+h)