n=list(map(int,input().strip().split()))
out=[]
 
 
out.append((n[1]*n[2])//n[6])
out.append(n[3]*n[4])
out.append(n[5]//n[7])
a=min(out)//n[0]
print(a)