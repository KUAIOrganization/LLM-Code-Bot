n, k = [int(i) for i in input().split()]

def main(n, k):
    letters = 'abcdefghijklmnopqrstuvwxyz'[:k]
    password = ''
    for i in range(n):
        password += letters[i%k]
    return password
print(main(n, k))