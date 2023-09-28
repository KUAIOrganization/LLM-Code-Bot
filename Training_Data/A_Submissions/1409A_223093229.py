NOT = int(input())
ans = []

def absolut(num1, num2):
    if num1>num2:
        return num1-num2
    else:
        return num2-num1

for n in range(NOT):
    line = [int(i) for i in input().split()]
    d = absolut(line[0], line[1])
    counter = d//10
    if d%10 !=0:
        counter+=1
    ans.append(counter)
for a in ans:
    print(a)