s=input()
s=s.lower()
for i in s:
    if i not in 'aeiouy':
        print('.',end=i)