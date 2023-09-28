alphabet=[chr(x) for x in range(65,91)]
word=input()
n=len(word)
sta=1
for i in range(1,n):
    if word[i] not in alphabet:
        sta=0
        break
if sta==0:
    print(word)
else:
    if word[0] in alphabet:
        print(word.lower())
    else:
        print(word.title())