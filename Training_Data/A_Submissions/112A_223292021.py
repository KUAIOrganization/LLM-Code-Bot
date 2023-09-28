fir=input().lower()
sec=input().lower()
ans=0
for i in range(len(fir)):
    if fir[i] > sec[i]:
        ans+=1;break
    elif fir[i] < sec[i]:
        ans-=1;break
print(ans)