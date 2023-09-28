t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    
    S = S.lower()
    S += "@"    
    S1 = ""
    for i in range(n):
        if S[i] != S[i+1]:
            S1 += S[i]
    
    if S1 == "meow":
        print("YES")
    else:
        print("NO")
        
        