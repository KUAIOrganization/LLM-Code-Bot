a=input()
b=['a','i','o','y','e','u']
for i in a:
    if i.lower() in b:
        continue
    else:
        print(f'.{i.lower()}',end='')