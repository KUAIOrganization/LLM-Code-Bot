chi=input()
ris=[int(xor) for xor in input().split()]
ris=sorted(ris,reverse=True)
van=1
while sum(ris[:van])<=sum(ris[van:]):
    van+=1
print(van)