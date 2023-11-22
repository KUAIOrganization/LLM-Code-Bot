r=input()
s=[]
for i in range(len(r)):
    s.append(r[i])
    
x=['A','E','I','O','U','Y','a','e','i','o','u','y']
y=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
z=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
w=[]
for i in range(len(s)):
   if s[i] in x:
       continue
   if s[i] in y:
       w.append('.')
       w.append(z[y.index(s[i])])
       continue
   if s[i] in z:
       w.append('.')
       w.append(z[z.index(s[i])])
       continue
print("".join(w))
   
   
