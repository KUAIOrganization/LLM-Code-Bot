num = int(input())
aim = list(map(int,input().split()))

result = []
count = 1
while count < num + 1:
    current = aim.index(count)
    result.append(current + 1)
    count += 1

string = ""
for number in result:
    string = string + str(number) + " "

print(string.rstrip())
    
    