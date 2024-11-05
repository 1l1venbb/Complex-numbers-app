def deleteNumber(lst , poz):
    '''

    Deletes the complex number found at the desired index.

    :param lst: List of complex numbers.
    :param poz: Integer that represents the index of the number that will be deleted.
    :return: List of complex numbers after being modified.
    '''

    lst.pop(poz)

    return lst

def deleteSequence(lst , poz):
    '''

    Deletes the sequence between the indexes found in poz.

    :param lst: List of complex numbers.
    :param poz: List that contains the start and end of the desired sequence.
    :return: List of complex numbers after being modified.
    '''

    i = poz[1] - poz[0] + 1

    while i > 0:
        lst.pop(poz[0])
        i -= 1

    return lst

def replaceNumber(lst , oldNumber , newNumber):
    '''

    Replaces all instances of oldNumber in lst with newNumber.

    :param lst: List of complex numbers.
    :param oldNumber: List that contains old complex number.
    :param newNumber: List that contains new complex number.
    :return: List after being modified.
    '''
    ok = False

    for i in range(len(lst)):
        if lst[i] == oldNumber:
            lst[i] = newNumber
            ok = True

    if ok:
        return lst
    else:
        raise ValueError