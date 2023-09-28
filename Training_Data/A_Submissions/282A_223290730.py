n=int(input())
outputs=0
for i in range(n):
    sta=input()
    if '++' in sta:
        outputs+=1
    else:
        outputs-=1
print(outputs)