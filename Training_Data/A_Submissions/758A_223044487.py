n = int(input())
a = list(map(int, input().split()))
maxBurle = max(a)
maxInd = a.index(maxBurle)
s = 0 #minimum Burles
for i in range(n):
  if a[i] < maxBurle:
    s += maxBurle - a[i]
print(s)