NOT = int(input())
ans = []
def get_the_difference(simmilar, array):
    dif = None
    for ar in range(len(array)):
        if array[ar] !=simmilar:
            dif = ar
            break
    return dif+1
    
for n in range(NOT):
    NOA = int(input())
    array = [int(i) for i in input().split()]
    a, b, c = tuple(array[:3])
    similar = a if a==c else b
    ans.append(get_the_difference(similar, array))
for a in ans:
    print(a)