n = int(input())
if n%2==0:
     a=[2]*(n//2)
     print(len(a))
     print(*a)
          
else:
     a=[2]*((n)//2)
     a.pop()
     a.append(3)
     print(len(a))
     print(*a)

          