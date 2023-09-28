numbers=[int(x) for x in input().split()]
numbers.sort()

a=numbers[-1]-numbers[0]
b=numbers[-1]-numbers[1]
c=numbers[-1]-numbers[2]



print(a,b,c)
