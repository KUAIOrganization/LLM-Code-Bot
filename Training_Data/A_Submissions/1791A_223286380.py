
t = int(input())
inp = []
for i in range(t):
    inp.append(input().strip())
s = "codeforces"
for i in inp:
    
    if i in s:
        print("YES")
    else:
        print("NO")

