import math
t = int(input())
for j in range(t):
    a, b, c, d = input().split()
    a = int(a) # time polycarp needs to sleep
    b = int(b) # time before first alarm
    c = int(c) # time for the rest of the alarms to go off
    d = int(d) # time for polycarp to sleep
    if a <= b:
        print(b)
    elif d >= c:
        print(-1)
    else:
        x = (a-b)/(c-d)
        x = math.ceil(x)
        time = (x*c) + b
        print(time)