import math
from . import reader
from . import other


def findNumbersInSequence(lst, poz):
    '''

    Returns the complex numbers in the sequence between poz[0] and poz[1].

    :param lst: List of complex numbers.
    :param poz: List with starting and ending indexes of the sequence.
    :return: List that contains the sequence.
    '''

    im = []
    for i in range(poz[0] , poz[1] + 1):
        im.append(lst[i])

    return im

def isModuleUnder10(lst):
    '''

    Returns the complex numbers with the module under 10.

    :param lst: List of complex numbers.
    :return: List that contains all complex numbers with the module under 10.
    '''
    rez = []

    for i in range(len(lst)):
        n = other.calculateModule(lst[i])
        if n < 10:
            rez.append(lst[i])

    return rez

def isModule10(lst):
    '''

    Returns the complex numbers with the module equal to 10.

    :param lst: List of complex numbers.
    :return: List that contains all complex numbers with the module equal to 10.
    '''
    rez = []

    for i in range(len(lst)):
        n = other.calculateModule(lst[i])
        if n == 10:
            rez.append(lst[i])

    return rez