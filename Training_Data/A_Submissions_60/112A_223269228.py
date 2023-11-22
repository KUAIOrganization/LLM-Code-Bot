def compare_strings(s1, s2):
    s1 = s1.casefold()  # Преобразуем строки к нижнему регистру
    s2 = s2.casefold()

    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Считываем две строки
string1 = input()
string2 = input()

# Вызываем функцию и выводим результат
result = compare_strings(string1, string2)
print(result)
