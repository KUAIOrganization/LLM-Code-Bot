def mex(n,k,x):
    if k>(x+1) or n<k:
        return -1
    if k==x:
        x = (x-1)
    sum = k*(k-1)//2 + (n-k)*x
    return sum

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k, x = (int(x) for x in input().split())
        print(mex(n,k,x))