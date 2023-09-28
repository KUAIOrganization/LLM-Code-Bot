letter=input()
letter=letter[1:-1]
flag=True
if len(letter)==0:
    flag=False
    print(0)
elif len(letter)==1:
    flag=False
    print(1)
elif flag:
    character=letter.split(", ")
    distinct=[]
    for char in character:
        if char not in distinct:
            distinct.append(char)
    print(len(distinct))