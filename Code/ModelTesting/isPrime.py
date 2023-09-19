def isPrime(number):
    primeMax = number**.5
    primeTest = 2
    while primeTest <= primeMax:
        if(number%primeTest == 0):
            return 0
        primeTest += 1
        if(primeTest != 3):
            primeTest += 1
    return number
