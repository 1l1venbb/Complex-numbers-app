def addNumberToList(lst , number):
    '''

    Adds a complex number at the end of the list.

    :param lst: List of complex numbers.
    :param number: Complex number (list).
    :return: List of complex numbers after being modified.
    '''

    lst.append(number)
    return lst

def insertNumberInList(lst, index, number):
    '''

    Inserts a complex number at a desired index in the list.

    :param lst: List of complex numbers.
    :param number: Complex number (list).
    :param index: Integer that represents the index of the insertion's location.
    :return: List of complex numbers after being modified.
    '''

    lst.insert(index , number)
    return lst
