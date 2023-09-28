n,k,l,c,d,p,nl,np=map(int,input().split())
ml=(k*l)/nl
lim=c*d
salt=p/np
print(int(min(ml,lim,salt)/n))