word = input()
letters = []

for i in range(len(word)):
    letters.append(word[i])

vowels = ['a','o','y','e','u','i']
consonants = ['b','c','d','f','g','h','j',
              'k','l','m','n','p','q','r',
              's','t','v','w','x','z']
outputs = []

for letter in letters:
    if letter.lower() in vowels:
        letter = ''
        outputs.append(letter)
    elif letter.lower() in consonants:
        letter ='.'+letter
        outputs.append(letter.lower())

output = ''
for x in outputs:
    output = output+x

print(output)
    
    
