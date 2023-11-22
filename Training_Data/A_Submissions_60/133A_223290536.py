n=str(input())
sgn=0
for s in n:
    if s=="H" or s=="Q" or s=="9":    sgn=1
if sgn==1:  print("YES")
else:   print("NO")