s=input()
up=s.upper()
f=0
z=0
ans=""
if s==up:
    z=1
    print(s.lower())
else:
    if s[0]==s[0].lower():
        for i in range(1,len(s)):
            if s[i]!=s[i].upper():
                f=1
        if f==0:
            ans+=s[0].upper()
            for i in range(1,len(s)):
                ans+=s[i].lower()
            z=1
            print(ans)
if z==0:
    print(s)