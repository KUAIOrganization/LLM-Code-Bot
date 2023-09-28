import math
t = int(input())
for i in range(t):
     s1,s2,s3,s4 =map(int,input().split())
     s = [s1,s2,s3,s4]
     m1 = max(s)
     m2 = 0
     for i in s:
          if i > m2 and i < m1:
               m2 = i
     if  m1 in s[:2] and m2 in s[:2]:
          print('NO')
     elif m1 in s[2:] and m2 in s[2:]:
          print('NO')
     else:
          print('YES')
     