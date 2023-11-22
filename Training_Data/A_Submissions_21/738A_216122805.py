n = int(input())
s = input()
o = ""
ind = 0
while ind < n:
    if (ind < n - 2 and s[ind] == 'o' and s[ind + 1] == 'g' and s[ind + 2] == 'o'):
        ind += 1
        o += "***"
        while (ind < n - 1 and s[ind] == 'g' and s[ind + 1] == 'o'):
            ind += 2
    else:
        o += s[ind]
        ind += 1
print(o)
