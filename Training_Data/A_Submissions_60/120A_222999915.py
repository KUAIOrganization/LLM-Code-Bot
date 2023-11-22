import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
n=int(input())
dic={('front',1):'L',('front',2):'R',('back',1):'R',('back',2):'L'}
print(dic[(s,n)])
