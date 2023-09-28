t=int(input())
for _ in range(t):
  l,r=map(int, input().split())
  x=l
  y=2*l
  if y<=r:
    print(str(x)+" "+str(y))
  else:
    print("-1 -1")
    
  