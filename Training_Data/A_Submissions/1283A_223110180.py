t = int(input())
for i in range(t):
     h,m = map(int,input().split())
     if h==0:
          print(24*60-m)
     else:
          print((24-h)*60-m)