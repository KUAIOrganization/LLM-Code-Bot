def solve():

    s=input()

    for i in range(26):
        if s.count(chr(ord('a')+i)):
            index=s.index(chr(ord('a')+i))
            print(chr(ord('a')+i) +' '+s[:index]+s[index+1:])
            return
    
for i in range(int(input())): solve()