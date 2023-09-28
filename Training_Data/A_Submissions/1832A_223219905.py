def plan(string):
    if len(string)%2==0:
        mid=int(len(string)/2)
        right=string[:mid]
        left=string[mid:]
    else:
        mid=int((len(string)-1)/2)
        right=string[:mid]
        left=string[mid+1:]
    letters=[]
    for letter in right:
        letters.append(letter)
    if len(set(letters))>1:
        print("YES")
    else:
        print('NO')
number_of_tests=input()
for test in range(int(number_of_tests)):
    string=input()
    plan(string)
 	 			  		   				  			  			 	 	