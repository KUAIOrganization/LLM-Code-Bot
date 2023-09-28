num_elements = int(input())
elements = input().split()
result = [elements.index(str(i + 1)) + 1 for i in range(num_elements)]
print(*result)
