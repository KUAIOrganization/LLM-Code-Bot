n, k = map(int,input().split())
fl = list(input())
c = 0
if fl.index('G') > fl.index('T'):
    for i in range(fl.index('G'),fl.index('T')-1,-k):
        if fl[i] == 'T':
            print('YES')
            c += 1
            break
        elif fl[i] == '#':
            break
    if c == 0: print('NO')
if fl.index('T') > fl.index('G'):
    for i in range(fl.index('G'),fl.index('T')+1,k):
        if fl[i] == 'T':
            print('YES')
            c += 1
            break
        elif fl[i] == '#':
            break         
    if c == 0: print('NO')