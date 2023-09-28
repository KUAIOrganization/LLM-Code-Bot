sdr=int(input(""))
for _ in range(sdr):
	pp=int(input(""))
	df=[int(x) for x in input("").split(" ")]
	sum=0
	for i in range(pp-1):
		if df[i]%2==df[i+1]%2:
		    sum+=1
	print(sum)