n = int(input())
s = input()
countA, countD = 0, 0
for i in range(len(s)):
    if s[i] == "D":
        countD+=1
    if s[i] == "A":
        countA+=1
if countA > countD:
    print("Anton")
elif countA < countD:
    print("Danik")
else:
    print("Friendship")