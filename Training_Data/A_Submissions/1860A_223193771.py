prefix = 'YES '
for line in [*open(0)][1:]:
    n = len(line) - 1
    result = ('NO', prefix + '(' * n + ')' * n, prefix + '()' * n)[-('((' in line or '))' in line) or ')(' in line]
    print(result)
