s1 = input().lower()
s2 = input().lower()
#aaaa  a = 97
#aaaA  A = 65
#abcdefg
#abcdeff
#acb
#abc
sz = len(s1)
i = 0
enter = 0
for i in range(sz):
    if s2[i] < s1[i]:
        print(1)
        enter = 1
        break

    elif s1[i] < s2[i]:
        print(-1)
        enter = 1
        break

    i += 1

if enter == 0:
    print(0)
