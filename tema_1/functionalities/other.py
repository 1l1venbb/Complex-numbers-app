import math

def calculateModule(number):
    '''

    Calculates the module of a complex number.

    :param number: List of 2 elements representing a complex number.
    :return: Module of the complex number.
    '''
    module = math.sqrt(getRealPart(number)**2 + getImaginaryPart(number)**2)
    return module

def isPrime(number):

    '''

    Checks if a number is prime or not.

    :param number: Number to be checked
    :return: True if number is prime, else False.
    '''

    ok = True

    if number < 2:
        return False
    if number == 2:
        return True

    if number % 2 == 0:
        return False


    i = 3
    while i * i <= number:
        if number % i == 0:
            ok = False
        i += 2

    return True

def getRealPart(lst):
    '''
    Returns the real part of a complex number.
    :param lst: Complex number.
    :return: int
    '''
    return lst["realPart"]

def getImaginaryPart(lst):
    '''
    Returns the imaginary part of a complex number.
    :param lst: Complex number.
    :return: int
    '''

    return lst["imaginaryPart"]