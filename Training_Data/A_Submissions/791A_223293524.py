str1=input().split()
Bob=int(str1[0])
Mark=int(str1[1])
i=0
while Bob<=Mark:
    Bob=Bob*3
    Mark=Mark*2
    i+=1
print(i)