a , b = map(int,input().split())
if (a+1)//2 < b:
    print(((b-(a + 1)//2) )*2)
if (a+1)//2 >=b:
    print((2*b)-1)
