test_case=int(input())
for i in range(test_case):
    nb_items = int(input())
    strArray = input()
    array = strArray.split(" ")
    nbNumero = 10 - nb_items
    
    denom = ((nbNumero*(nbNumero-1))/2*6)

    print(int(denom))