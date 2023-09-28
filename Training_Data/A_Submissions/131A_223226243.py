x = input()
if x.isupper():
    print(x.lower())
else:
    if str(x[0]).islower():
        y = x[0]
        if len(x) == 1:
            print(x.swapcase())
        else:
            x = x[1:]
            if x.isupper():
                x = y + x[0:]
                print(x.swapcase())
            else:
                x = y + x[0:]
                print(x)
    else:
        print(x)
            
