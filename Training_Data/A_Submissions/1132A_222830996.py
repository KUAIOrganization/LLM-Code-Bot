cnt = []
for i in range(4):
	cnt.append(int(input()))
if(cnt[0] == cnt[3] and (cnt[2] == 0 or cnt[0] > 0)):
	print(1)
else:
	print(0)