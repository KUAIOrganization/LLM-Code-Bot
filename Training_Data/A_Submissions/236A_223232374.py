user_name = input()
letters = []
keys = []
n = len(user_name)

for i in range(n):
    a = user_name[i]
    letters.append(a)

for letter in letters:
    if letter not in keys:
        keys.append(letter)
    else:
        pass

m = len(keys)
if m%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

    
