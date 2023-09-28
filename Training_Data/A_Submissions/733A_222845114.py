s = str(input())
i = 0
prev_count = 0
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

while i < len(s):
    count = 1
    while i < len(s) and s[i] not in vowels:
        i+=1
        count+=1
    i+=1
    if count > prev_count:
        prev_count = count
        count = 1
    elif count < prev_count or count == prev_count:
        count = 1
        

print(prev_count)
    
            
    
