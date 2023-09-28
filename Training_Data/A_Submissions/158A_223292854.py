x=input()
y=x.split()
n,k=int(y[0]),int(y[1])
a=input()
m=a.split()
count=0
b=0
for i in m:
      if int(i)>0:
        b=1            
if b==1:
    for i in m:
            if int(i)>=int(m[k-1]) and int(i)>0:
                count+=1
print(count)

    



    