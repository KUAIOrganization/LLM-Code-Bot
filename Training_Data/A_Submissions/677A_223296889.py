n,h =map(int, input().split())
for i in map(int, input().split()):
    if i > h:
        n+=1
print(n)