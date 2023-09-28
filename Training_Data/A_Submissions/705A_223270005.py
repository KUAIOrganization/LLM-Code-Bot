x=int(input())
c='I hate'
for i in range(x-1):
    c+=' that'
    if i%2==0:c+=' I love'
    else:c+=' I hate'
print(c+' it')