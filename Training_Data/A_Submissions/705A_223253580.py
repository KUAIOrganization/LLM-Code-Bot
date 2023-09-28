n=int(input())

for i in range(1,n+1):
    
    if(i%2==0 and i!=n):
        print("I love that",end=" ")
    elif (i%2!=0 and i!=n):
        print("I hate that",end=" ")
    elif (i%2==0 and i==n):
        print("I love it")
    elif(i%2!=0 and i==n):
        print("I hate it")
