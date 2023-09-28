n=int(input())
s=input()
if s.count('A')==s.count('D'):
    c="Friendship"
else:
   c= "Anton" if s.count('A')>s.count('D') else "Danik" 
print(c)
    