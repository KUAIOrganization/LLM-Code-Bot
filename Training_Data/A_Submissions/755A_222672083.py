n = int(input())
def prime(x):
  counter = 0
  for i in range(2,x):
    if x%i == 0:
      counter += 1
      break
  if counter == 0:
    return 1
  else:
    return 0
m = 1
while prime(m*n+1) == 1:
  m += 1
print(m)