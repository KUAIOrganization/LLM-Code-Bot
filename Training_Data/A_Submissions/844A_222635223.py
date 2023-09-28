a=input()
n=len(a)
k=int(input())
print([max(0,k-len({*a})),'impossible'][n<k])