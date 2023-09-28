
import math

n , m , i , j , a , b = [int(x) for x in input().split()]
corners = [(n ** k, m ** z) for z in range(2) for k in range(2 )]
minSteps = math.inf

# 1
# 1
# 1
# 1
# 1

# 1 1 o 1 1

for c in corners:
    steps = (abs(c[0] - i) , abs(c[1] - j))
   
    if steps[0] % a != 0 or steps[1] % b != 0:
        continue
    
    if (max(steps[1] , m - 1 - steps[1]) < b or max(steps[0] , n - 1 - steps[0]) < a) and not steps == (0 , 0):
        continue
    
    # print(c , "=>" , steps)

    maxStepsA = steps[0] // a
    maxStepsB = steps[1] // b

    if maxStepsA % 2 != maxStepsB % 2:
        continue

    minSteps = min(minSteps , max(maxStepsA , maxStepsB))

if minSteps == math.inf:
    print("Poor Inna and pony!")
else:
    print(minSteps)