t=int(input())
mas=[]
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    current_pos = 0
    while k>0:
        while current_pos < len(a) and a[current_pos] == 0:
            current_pos += 1

        if current_pos >= len(a):
            break
        a[current_pos] -=1 
        a[-1] += 1        
        k-=1

    mas.append(a)

for i in mas:
    print(*i)

