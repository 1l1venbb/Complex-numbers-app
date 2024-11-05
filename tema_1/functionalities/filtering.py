from . import other

def filterPrime(lst):
    '''

    Returns a list that contains the complex numbers which have the real part different from prime numbers

    :param lst: List of complex numbers.
    :return: List of complex numbers.
    '''
    rez = []

    for j in range(len(lst)):

        ok = other.isPrime(other.getRealPart(lst[j]))

        if not ok:
            rez.append(lst[j])

    return rez

def filterHigherModule(lst, module):
    '''

    Returns a list that contains all complex numbers with their modules higher than module.

    :param lst: List of complex numbers.
    :param module: Target module.
    :return: List of complex numbers.
    '''
    rez = []

    for i in range(len(lst)):
        if module < other.calculateModule(lst[i]):
            rez.append(lst[i])

    return rez

def filterLowerModule(lst, module):
    '''

    Returns a list that contains all complex numbers with their modules lower than module.
    :param lst: List of complex numbers.
    :param module: Target module.
    :return: List of complex numbers.
    '''

    rez = []

    for i in range(len(lst)):
        if module > other.calculateModule(lst[i]):
            rez.append(lst[i])

    return rez

def filterEqualModule(lst, module):
    '''
    Returns a list that contains all complex numbers with their modules equal to the module.
    :param lst: List of complex numbers.
    :param module: Target module.
    :return: List of complex numbers.
    '''

    rez = []
    for i in range(len(lst)):
        if module == other.calculateModule(lst[i]):
            rez.append(lst[i])

    return rez