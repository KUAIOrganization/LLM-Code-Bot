#JAI MATA DI
##### binary and decimal #####
#  way to convert number to binary ------->  bin(Number)[2:] 
# way to convert binary to number ------->  int(n,2)
#########################
#to get permutations of a string
from itertools import permutations
def allPermutations(str):
    permList = permutations(str)
    return permList
#######################
# TO GET FACTORS OF A NUMBER:
def factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i: 
                result.append(x//i)
        i += 1
    return result
#####################################
def fast_expo(val, power):
    result = pow(val, power//2)
    result = result * result
 
    if power % 2 != 0:
        result = result * val
    return result
######################################
# check if prime or not
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
#######################################    
t=int(input())
i=0
while i<t:
    n,m=map(int,input().split())
    l=[]
    e=[]
    for j in range(n):
        lst=list(map(int,input().split()))
        
            
        for x in range(len(lst)):
            maxi=max(lst)
            if lst[x]==maxi:
                l.append([j+1,x+1])
                e.append(maxi)
    #print(l)
    #print(e)
    for j in range(n):
        o=max(e)
        #print(o)
        if e[j]==o:
            y=l[j][0]
            w=l[j][1]
            
            print((n-min(n-y,y-1))*(m-min(m-w,w-1)))



    i+=1


    
