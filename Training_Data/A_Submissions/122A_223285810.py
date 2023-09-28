num=int(input())
if num%4==0 or num%7==0:
    print('YES')
elif num%44==0 or num%77==0 or num%47==0 or num%74==0:
    print("YES")
elif num%444==0 or num%447==0 or num%474==0 or num%477==0:
    print('YES')
elif num%744==0 or num%747==0 or num%774==0 or num%777==0:
    print('YES')
else:
    print("NO")
