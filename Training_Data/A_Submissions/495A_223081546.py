
n = int(input())
 
possible = {"0":2, "1":7, "2":2, "3":3, "4":3, "5":4, "6":2, "7":5, "8":1, "9":2}
 
if len(str(n)) == 1:
    a = '0' + str(n)
else:
    a = str(n)
 
first = possible[a[0]]
second = possible[a[1]]
 
print(first*second)