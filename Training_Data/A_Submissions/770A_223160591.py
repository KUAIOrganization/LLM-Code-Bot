n,k= [int(x) for x in input().split()]
i=0
char=97
l=[]
while i<n:
    if i<k:
        l.append(chr(char))
    i+=1
    char+=1
i=0
while i<n-k:
    l.append(l[i])
    i+=1

print(''.join(l))
    
    
    
        