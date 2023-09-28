def rearrange_sum(s):
    # Извлекаем все числа из строки и сортируем их
    numbers = sorted([int(char) for char in s if char.isdigit()])
    
    # Формируем новую строку с числами
    new_sum = '+'.join(map(str, numbers))

    return new_sum

# Считываем входные данные
s = input()

# Вызываем функцию и выводим результат
result = rearrange_sum(s)
print(result)
