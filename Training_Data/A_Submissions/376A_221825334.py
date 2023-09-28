def solve(s1: str) -> str:
    s= list(s1.strip(" "))
    left=0
    right=0
    pivot=s.index("^")
    for x in range(0,pivot):
        if s[x]!='=':
            left+=int(s[x])*(pivot-x)
    for x in range(pivot+1,len(s)):
        if s[x]!='=':
            right+=int(s[x])*(x-pivot)
    if left>right:
        return('left')
    elif right>left:
        return('right')
    else:
        return('balance')
s1 = str(input())
print(solve(s1))
    
