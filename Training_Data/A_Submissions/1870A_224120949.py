for _ in range(int(input())):
  n,k,x=map(int,input().split())
  if n<k or k>x+1:
    print(-1)
  else:
    if(x!=k):
      result=k*(k-1)/2
      result=result+(x)*(n-k)
    else:
      result=k*(k-1)/2
      result=result+(x-1)*(n-k)
    print(int(result))