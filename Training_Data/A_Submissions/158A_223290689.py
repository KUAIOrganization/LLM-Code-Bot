n = list(map(int,input().split()))
score = list(map(int,input().split()))
standard = score[n[1]-1]
count = 0
for i in score:
    if i >= standard and i > 0:
        count += 1
print(count)