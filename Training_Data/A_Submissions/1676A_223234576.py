def sum_of_numbers(n):
    summa = 0
    for digit in n:
        summa += int(digit)
    return summa
t = int(input())
for i in range(t):
    s = input()
    left_sum = sum_of_numbers(s[:3])
    right_sum = sum_of_numbers(s[3:])
    if left_sum == right_sum:
        print('YES')
    else:
        print('NO')