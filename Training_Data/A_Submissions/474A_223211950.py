c=input()
s=input()
a="qwertyuiopasdfghjkl;zxcvbnm,./"
q=""
if c=='R':
    for i in range(0,len(s)):
        t=a.find(s[i])
        if s[i]=='q':
            q+="/"
        else:
            q+=a[t-1]
else:
    for i in range(0,len(s)):
        t=a.find(s[i])
        if s[i]=='/':
            q+="q"
        else:
            q+=a[t+1]
print(q)
