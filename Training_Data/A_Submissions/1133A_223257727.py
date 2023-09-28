x=input().split(":")
y=input().split(":")
a=[int(i) for i in x]
b=[int(i) for i in y]
total_diff=(b[0]-a[0])*60+(b[1]-a[1])
req=total_diff//2
c1=req//60
c2=req-60*c1
ans1=a[0]+c1
ans2=a[1]+c2
if ans2>=60:
    ans1+=1
    ans2=ans2-60
if len(str(ans1))==1:
    ans1="0"+str(ans1)
else:
    ans1=str(ans1)
if len(str(ans2))==1:
    ans2="0"+str(ans2)
else:
    ans2=str(ans2)
print("{}:{}".format(ans1,ans2))
