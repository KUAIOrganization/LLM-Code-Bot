s = input()
if (s[0].swapcase() == s[0].upper() and s[1:].swapcase() == s[1:].lower()):
    s= s.capitalize()
elif s.swapcase() == s.lower():
    s = s.lower()
print(s)