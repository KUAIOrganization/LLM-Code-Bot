T = int(input())
for i in range(T):
    K = int(input())
    cnt = 0
    L = 0
    while(cnt<K):
        L = L+1
        if(L%3!=0 and L%10!=3):
            cnt = cnt+1
    print(L)