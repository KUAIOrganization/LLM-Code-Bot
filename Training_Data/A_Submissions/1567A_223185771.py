for _ in range(int(input())):
    n=int(input())
    s=input()
    if(s.count("D")==0):
        print(s.replace("U","D"))
    else:
        print(s.replace("D","U"))