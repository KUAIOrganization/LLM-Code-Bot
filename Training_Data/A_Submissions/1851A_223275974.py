for i in range (int(input())):
    n, m, k, H = map(int, input().split())
    a= list(map(int,input().split()))
    diff = []
    output =0
    for j in range (n):
        diff.append(abs(H-a[j]))
    for l in range (n):
        if(diff[l]%k==0 and diff[l]/k < m and diff[l]!=0):
           output = output +1 
            
    print(output)