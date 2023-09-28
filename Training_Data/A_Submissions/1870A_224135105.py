
def solve(n,k,x):
    if(n<k):
        return (-1)
    if(x<k-1):
        return (-1)
    total = 0
    for i in range(n):
        if i<k:
            total+=i
        else:
            if k==x:
                total+=x-1
            else:
                total+=x
        # print("total loop,",total)
    return(total)

    

t = int(input())
for i in range(t):
    txt = input()
    n,k,x = list(map(int,txt.split(" ")))
    print(solve(n,k,x))

# solve(6,7,[1,2,7,3,6,4])