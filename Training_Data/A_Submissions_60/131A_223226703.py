a=input()
a=str(a)
b=[]
j=0
l=""
for i in a[1:] :
    if(i.islower()==True):
        j=1
if (j==0):
    for k in a:
        b.append(k.swapcase())
    for m in b:
        l+=m
    print(l)

else:
    print(a)
        
        
 
            
            
    
    
