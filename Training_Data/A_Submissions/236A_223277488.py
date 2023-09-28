s = input().strip()
dist_dic = {}
for i in s:
    dist_dic[i] = None
dist_ch = list(dist_dic.keys())

if len(dist_ch) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
