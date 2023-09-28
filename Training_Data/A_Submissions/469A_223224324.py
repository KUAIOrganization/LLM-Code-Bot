stages = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
togglebreak = False
del x[0]
del y[0]
for a in range(stages):
    if (a+1) not in x and (a+1) not in y:
        print('Oh, my keyboard!')
        togglebreak = True
        break
if togglebreak == False:
    print('I become the guy.')