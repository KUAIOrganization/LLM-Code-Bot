def solve():
  n,k,x = map(int, input().split())
  s = -1
  if k > n:
    s = -1
  elif k - 1 > x:
    s = -1
  elif x == k:
    s = (k * (k - 1)) // 2 + (n - k) * (k - 1)
  else:
    s = (k * (k - 1)) // 2 + (n - k) * x
  print(s)
  return

if __name__ == '__main__':
  # t = 1
  t = int(input())
  while t > 0:
    t -= 1
    solve()