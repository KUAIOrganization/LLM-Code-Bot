def f(x,p,a):
  return x+min(p-2*x,(a-x)//2)

def solve(p,a):
  lmin=0
  lmax=min(p//2,a)
  while lmax-lmin>2:
    x1,x2=(2*lmin+lmax)//3,(lmin+2*lmax)//3
    f1,f2=f(x1,p,a),f(x2,p,a)
    lmin,lmax=(lmin,x2)if f1>f2 else (x1,lmax)
  return max(f(lmin,p,a),f(lmin+1,p,a),f(lmax,p,a))

for t in range(int(input())):
  p,a=map(int,input().split())
  print(solve(p,a))
