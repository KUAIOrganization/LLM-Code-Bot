n=int(input())
s=0
for i in range(n):
    x=str(input())
    
    if (x=="Tetrahedron"):
        s+=4
    
    elif(x=="Cube"): 
        s+=6
    elif(x=="Octahedron"):
        s+=8
        
    elif(x=="Dodecahedron"):
        s+=12
        
    elif(x=="Icosahedron"):
        s+=20
print(s)        