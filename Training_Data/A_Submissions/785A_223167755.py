n=int(input())
s=0
for i in range(n):
    a=input()
    if a=='Tetrahedron':
        s+=4
    elif a=='Cube':
        s+=6
    elif a=='Octahedron':
        s+=8
    elif a=='Dodecahedron':
        s+=12
    elif a=='Icosahedron':
        s+=20
print(s)