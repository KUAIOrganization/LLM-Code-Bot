class Solution:
	def __init__(self):
		pass

	def solve(self):
		n = int(input())
		
		if n % 4 == 0:
			print(0)
		elif n % 4 == 1:
			print(1)
		elif n % 4 == 2:
			print(1)
		elif n % 4 == 3:
			print(0)	


if __name__ == "__main__":
	sol = Solution()
	sol.solve()
