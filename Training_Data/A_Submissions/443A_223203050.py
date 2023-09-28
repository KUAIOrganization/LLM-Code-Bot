import re
a=input()
a=re.split(' |,|{|}',a)
a=set(a)
print(len(a)-1)