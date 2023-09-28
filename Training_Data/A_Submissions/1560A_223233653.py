def generate_sequence():
    n = 1
    while True:
        if n % 3 != 0 and n % 10 != 3:
            yield n
        n += 1

# Чтение количества наборов данных
t = int(input())

# Для каждого набора данных
for _ in range(t):
    # Чтение значения k
    k = int(input())

    # Создаем генератор последовательности
    sequence = generate_sequence()

    # Находим k-й элемент последовательности
    for _ in range(k):
        x = next(sequence)

    # Выводим результат
    print(x)
