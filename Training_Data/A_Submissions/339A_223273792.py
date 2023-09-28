s = input().strip()
digits = [int(ch) for ch in s if ch.isdigit()]
digits.sort()
newS = "+".join(map(str, digits))
print(newS)
