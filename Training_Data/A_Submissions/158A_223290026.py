inputs=input().split()
n=int(inputs[0]);k=int(inputs[1])
scores=list(map(int,input().split()))
scores.append(0)
num_0=scores.index(0)
equal=scores[k-1]
scores.sort()
num=len(scores)-scores.index(equal)
print(min(num,num_0))