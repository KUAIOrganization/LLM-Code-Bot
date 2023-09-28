# Подумать а шо происходит япона мать

n , m= map(int, input().split())
array = []
found = False

C = 'C' #cyan
M = 'M' #magenta
Y = 'Y' #yellow

W = 'W' #white
G = 'G' #grey
B = 'B' #black

for i in range (n):
    row = input().split()
    if len(row) != m:
        exit()
    array.append(row)

for i in range(n):
    for j in range(m):
        if array[i][j] == C:
            found = True
            break
        if array[i][j] == M:
            found = True
            break
        if array[i][j] == Y:
            found = True
            break
        

if found:
   print('#Color')
            
if not found:
    print('#Black&White')


