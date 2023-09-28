for case in range(int(input())):
  num = 0
  n, m, k, H = map(int, input().split())
  h = list(map(int, input().split()))
  for i in range(n):
    diff = abs(H - h[i])
    if diff%k == 0 and diff//k < m and diff//k!=0:
      num += 1
  print(num)
