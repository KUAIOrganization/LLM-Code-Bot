def read():
	return int(input())
def read_list():
	return [int(x) for x in input().split(' ')]




for _ in range(read()):
	n, k, x = read_list()
	result = 0
	if k > n or k > x+1:
		print(-1)
		continue
	for i in range(n):
		if i < k: 
			result += i
		else:
			if x != k: 
				result += x 
			else: 
				result += k-1

	print(result)
