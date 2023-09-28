def  Odd_Divisor(n) :
    """
    :param n: 
    :return: this loop helps efficiently identify whether there exists an odd divisor greater than one 
    by removing all the factors of 2 from n. 
    If n is greater than 1 after this process, it means an odd divisor exists, and we return True
    """
    while n % 2 == 0:
        n //= 2
    return n > 1
if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        if Odd_Divisor(n):
            print("YES")
        else :
            print("NO")
