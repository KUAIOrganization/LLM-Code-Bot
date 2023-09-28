n=int(input())
s=input().split()
s1=set()
for i in range(n):
    s0=set()
    for j in range(len(s[i])):
        s0.add(s[i][j])
    s1.add(str(sorted(list(s0))))
print(len(s1))