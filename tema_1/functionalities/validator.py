def validateIndex(n):
    '''

    Validates initial length of the list

    :param n: length to validate
    :return: ValueError for invalid length.
    '''
    if n < 0:
        raise ValueError("Index is out of range.")

def validateIndexInList(lst, poz):
    '''

    Checks if the index is in the list.

    :param lst: List of complex numbers.
    :param poz: Index to validate
    :return: ValueError for invalid index.
    '''

    if poz < 0 or poz >= len(lst):
        raise ValueError("Index is out of range.")

def validateSequenceIndex(lst, poz):

    '''

    Checks if the sequence exists in the list.

    :param lst: List of complex numbers.
    :param poz: Start and end of the sequence.
    :return: raises ValueError if the sequence does not exist.
    '''

    if poz[0] < 0 or poz[0] >= len(lst) or poz[1] < 0 or poz[1] >= len(lst):
        raise ValueError("Index is out of range.")

def validateOption(option, poz):
    '''
    Validates option.
    :param option: Option to validate.
    :param poz: range in which the option is valid.
    :return: ValueError for invalid option.
    '''
    if option < poz[0] or option > poz[1]:
        raise ValueError("Invalid option.")