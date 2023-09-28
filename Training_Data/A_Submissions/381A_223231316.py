n=int(input())
arr=list(map(int,input().strip().split()))
i=0
j=len(arr)-1
a=0
b=0
flag=0
while(i<=j):
    if(flag==0):
        flag=1
        if(arr[i]>arr[j]):
            a=a+arr[i]
            i=i+1
        else:
            a=a+arr[j]
            j=j-1
    else:
        flag=0
        if(arr[i]>arr[j]):
            b=b+arr[i]
            i=i+1
        else:
            b=b+arr[j]
            j=j-1
print(str(a) + " "+ str(b))        
        
            
    
    