n = int(input())
s = ""
for i in range(n):
    if i % 2:
        s+= "I love"
    else:
        s+= "I hate"
    if i + 1 < n:
        s+= " that "
    else:
        s+= " it"
print(s)