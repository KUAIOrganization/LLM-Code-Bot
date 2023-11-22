inp=input()
vowels=["a","e","i","o","u","y"]
out=""
result=""
lower=inp.lower()
for i in lower:
    if i not in vowels:
        out+=i
for i in out:
    result=result+"."+i
print(result)