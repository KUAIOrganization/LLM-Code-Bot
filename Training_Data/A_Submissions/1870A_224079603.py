for _ in range(int(input())):
  n,x,k=[int(i) for i in input().split()]
  c=0
  s=0
  f=False
  if x>n or x-1>k:
    print(-1)
    continue
  while c<n+1:
    if c==x:
      f=True
      c+=1
      continue
    if f:
      if k==x:
        k-=1
      s+=k
    else:
      s+=c
    c+=1
  print(s)