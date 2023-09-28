(n,k,l,c,d,p,nl,np)=map(int,input().split(' '))
a =((k*l)//nl)//n
b=(c*d)//n
c=(p//np)//n
print(min(a,b,c))