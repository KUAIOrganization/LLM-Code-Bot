# print(max(0 , minimum))

n = int(input())

x , y  = set() , set()
for i in range(n):
    input_ = input().split()
    x.add(input_[0])
    y.add(input_[1])

print(min(len(x) , len(y)))