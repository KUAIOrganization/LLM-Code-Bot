def factorial(number):
    if not (type(number) == int):
        raise ValueError("Can only take factorial of ints!")
    if number < 0:
        raise ValueError("Cannot take factorial of negative number!")
    if number == 0:
        return 1
    return number * factorial(number - 1)
