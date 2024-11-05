import functionalities.addToList as lstadd
import functionalities.modifyList as modify
import functionalities.searchInList as search
import functionalities.filtering as filtering
import functionalities.other as other
import functionalities.operations as operations
import functionalities.validator as validator
import functionalities.undo as undo

import functionalities.writer as writer

def test_validateIndex():
    '''

    Test function for validateIndex()

    '''
    a = -1
    try:
        validator.validateIndex(a)
        assert False
    except ValueError:
        assert True

        a = 1
        try:
            validator.validateIndex(a)
            assert True
        except ValueError:
            assert False

def test_validateSequenceIndex():
    '''

    Test function for validateSequenceIndex()

    '''
    lst = [{"realPart" : 1 , "imaginaryPart" : 1} , {"realPart" : 1 , "imaginaryPart" : 1} , {"realPart" : 1 , "imaginaryPart" : 1} , {"realPart" : 1 , "imaginaryPart" : 1}]

    a = [0 , 8]
    try:
        validator.validateSequenceIndex(lst, a)
        assert False
    except ValueError:
        assert True


    a = [-1 , 3]
    try:
        validator.validateSequenceIndex(lst , a)
        assert False
    except ValueError:
        assert True

    a = [0 , 1]
    try:
        validator.validateSequenceIndex(lst , a)
        assert True
    except ValueError:
        assert False

def test_validateOption():

    option = 3
    poz = [1, 4]

    try:
        validator.validateOption(option, poz)
        assert True
    except ValueError:
        assert False

    option = 10
    poz = [1, 4]

    try:
        validator.validateOption(option, poz)
        assert False
    except ValueError:
        assert True

def  test_addNumberToList():
    '''

    Test function for addNumberToList()

    '''
    lst = [{"realPart" : 1 , "imaginaryPart" : 2} , {"realPart" : 3 , "imaginaryPart" : 3} , {"realPart" : 2 , "imaginaryPart" : 4}]
    assert lstadd.addNumberToList(lst, {"realPart" : 10, "imaginaryPart" :11}) == [{"realPart" : 1 , "imaginaryPart" : 2} , {"realPart" : 3 , "imaginaryPart" : 3} , {"realPart" : 2 , "imaginaryPart":4} , {"realPart" : 10 , "imaginaryPart" : 11}]

def test_insertNumberInList():

    '''
    Test function for insertNumberInList()
    '''

    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}]

    assert lstadd.insertNumberInList(lst, 1 , {"realPart" : 10 , "imaginaryPart" : 11}) == [{"realPart" : 1 , "imaginaryPart" : 2} , {"realPart" : 10 , "imaginaryPart" : 11}  ,{"realPart" : 3 , "imaginaryPart" : 3} , {"realPart" : 2 , "imaginaryPart" : 4}]


    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}]
    assert lstadd.insertNumberInList(lst, 2, {"realPart" : 10 , "imaginaryPart" : 11}) == [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
                                                                                           {"realPart" : 10 , "imaginaryPart" : 11}, {"realPart": 2, "imaginaryPart": 4}]

def test_deleteNumber():
    '''

    Test function for deleteNumber()

    '''
    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}]
    assert modify.deleteNumber(lst, 1) == [{"realPart": 1, "imaginaryPart": 2},
           {"realPart": 2, "imaginaryPart": 4}]

    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}]
    assert modify.deleteNumber(lst, 2) == [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3}]

def test_deleteSequence():
    '''

    Test function for deleteSequence()

    '''
    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 3}]
    poz = [2, 4]

    assert  modify.deleteSequence(lst, poz) == [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3}, {"realPart": 6, "imaginaryPart": 3}]

    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 3}]

    poz = [2, 5]

    assert  modify.deleteSequence(lst, poz) == [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3}]

def test_replaceNumber():
    '''

    Test function for replaceNumber()

    '''
    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 3}]

    assert modify.replaceNumber(lst, {"realPart": 1, "imaginaryPart": 2} , {"realPart": 10, "imaginaryPart": 12}) == [{"realPart": 10, "imaginaryPart": 12}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 3}]


    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 1, "imaginaryPart": 2}, {"realPart": 2, "imaginaryPart": 4}]

    assert modify.replaceNumber(lst, {"realPart": 2, "imaginaryPart": 4}, {"realPart": 11, "imaginaryPart": 13}) == [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 11, "imaginaryPart": 13}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 1, "imaginaryPart": 2}, {"realPart": 11, "imaginaryPart": 13}]

def test_findNumbersInSequence():
    '''
    Test function for findNumbersInSequence()
    '''
    lst = [{"realPart": 1, "imaginaryPart": 2}, {"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 3}]

    assert search.findNumbersInSequence(lst, [1 , 3]) == [{"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": 5}]
    assert search.findNumbersInSequence(lst, [1, 2]) == [{"realPart": 3, "imaginaryPart": 3},
           {"realPart": 2, "imaginaryPart": 4}]

def test_isModuleUnder10():
    '''
    Test function for isModuleUnder10()
    '''
    lst = [{"realPart": 1, "imaginaryPart": 11}, {"realPart": 3, "imaginaryPart": 5}, {"realPart": 8, "imaginaryPart": 4}, {"realPart": 14, "imaginaryPart": 5}, {"realPart": 8, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 10}]
    assert search.isModuleUnder10(lst) == [{"realPart": 3, "imaginaryPart": 5} , {"realPart": 8, "imaginaryPart": 4} , {"realPart": 8, "imaginaryPart": 2}]

    lst = []
    assert search.isModuleUnder10(lst) == []

def test_isModule10():
    '''
    Test function for isModule10()
    '''
    lst = [{"realPart": 1, "imaginaryPart": 11}, {"realPart": 3, "imaginaryPart": 5},
           {"realPart": 8, "imaginaryPart": 4}, {"realPart": 14, "imaginaryPart": 5},
           {"realPart": 8, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 8}]

    assert search.isModule10(lst) == [{"realPart": 6, "imaginaryPart": 8}]

    lst = []
    assert search.isModule10(lst) == []

def test_filterPrime():
    '''
    Test function for filterPrime()
    '''
    lst = [{"realPart": 2, "imaginaryPart": 3} , {"realPart": 5, "imaginaryPart": 4} , {"realPart": 4, "imaginaryPart": 5} , {"realPart": 8, "imaginaryPart": 8} , {"realPart": 7, "imaginaryPart": 8} , {"realPart": 1, "imaginaryPart": 2}]
    assert filtering.filterPrime(lst) == [{"realPart": 4, "imaginaryPart": 5} , {"realPart": 8, "imaginaryPart": 8} , {"realPart": 1, "imaginaryPart": 2}]

    lst = []
    assert filtering.filterPrime(lst) == []

def test_isPrime():

    '''
    Test function for isPrime()
    '''

    assert other.isPrime(0) == False
    assert other.isPrime(1) == False
    assert other.isPrime(2) == True
    assert other.isPrime(3) == True
    assert other.isPrime(19) == True

def test_calculateModule():
    '''
    Test function for calculateModule()
    '''
    assert other.calculateModule({"realPart": 3, "imaginaryPart": 4}) == 5
    assert other.calculateModule({"realPart": -3, "imaginaryPart": -4}) == 5
    assert other.calculateModule({"realPart": 0, "imaginaryPart": 5}) == 5
    assert other.calculateModule({"realPart": 0, "imaginaryPart": 0}) == 0
    assert other.calculateModule({"realPart": 0.6, "imaginaryPart": 0.8}) == 1

def test_filterHigherModule():
    '''
    Test function for filterHigherModule()
    '''

    lst = [{"realPart": 1, "imaginaryPart": 11},
    {"realPart": 3, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 4},
    {"realPart": 14, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 10}]
    assert filtering.filterHigherModule(lst, 8) == [{"realPart": 1, "imaginaryPart": 11} , {"realPart": 8, "imaginaryPart": 4},
    {"realPart": 14, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 10}]

    lst = [ {"realPart": 3, "imaginaryPart": 4},
    {"realPart": 3, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 4},
    {"realPart": 4, "imaginaryPart": -3},
    {"realPart": -3, "imaginaryPart": -4},
    {"realPart": 6, "imaginaryPart": 10},
    {"realPart": 1, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 6}]
    assert filtering.filterEqualModule(lst, 1000) == []

def test_filterLowerModule():
    '''
    Test function for filterLowerModule()
    '''
    lst = [  {"realPart": 1, "imaginaryPart": 11},
    {"realPart": 3, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 4},
    {"realPart": 14, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 10},
    {"realPart": 1, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 6}]
    assert filtering.filterLowerModule(lst, 8) == [{"realPart": 3, "imaginaryPart": 5} , {"realPart": 1, "imaginaryPart": 2}]

    lst = [ {"realPart": 3, "imaginaryPart": 4},
    {"realPart": 3, "imaginaryPart": 5},
    {"realPart": 8, "imaginaryPart": 4},
    {"realPart": 4, "imaginaryPart": -3},
    {"realPart": -3, "imaginaryPart": -4},
    {"realPart": 6, "imaginaryPart": 10},
    {"realPart": 1, "imaginaryPart": 2},
    {"realPart": 6, "imaginaryPart": 6}]

    assert filtering.filterEqualModule(lst, 1) == []

def test_filterEqualModule():
    '''
    Test function for filterEqualModule()
    '''
    lst = [{"realPart": 3, "imaginaryPart": 4},
           {"realPart": 3, "imaginaryPart": 5},
           {"realPart": 8, "imaginaryPart": 4},
           {"realPart": 4, "imaginaryPart": -3},
           {"realPart": -3, "imaginaryPart": -4},
           {"realPart": 6, "imaginaryPart": 10},
           {"realPart": 1, "imaginaryPart": 2},
           {"realPart": 6, "imaginaryPart": 6}]
    assert filtering.filterEqualModule(lst, 5) == [{"realPart": 3, "imaginaryPart": 4} ,  {"realPart": 4, "imaginaryPart": -3} , {"realPart": -3, "imaginaryPart": -4}]

    lst = [{"realPart": 3, "imaginaryPart": 4},
           {"realPart": 3, "imaginaryPart": 5},
           {"realPart": 8, "imaginaryPart": 4},
           {"realPart": 4, "imaginaryPart": -3},
           {"realPart": -3, "imaginaryPart": -4},
           {"realPart": 6, "imaginaryPart": 10},
           {"realPart": 1, "imaginaryPart": 2},
           {"realPart": 6, "imaginaryPart": 6}]
    assert filtering.filterEqualModule(lst, 6) == []

def test_calculateSequenceSum():
    '''
    Test function for calculateSequenceSum()
    '''

    lst = [{"realPart": 3 , "imaginaryPart": 4},{"realPart": 3 , "imaginaryPart": 5}, {"realPart": 8 , "imaginaryPart": 4}, {"realPart": 4 , "imaginaryPart": -3}, {"realPart": -3 , "imaginaryPart": -4}, {"realPart": 6 , "imaginaryPart": 10}, {"realPart": 1 , "imaginaryPart": 2}, {"realPart": 6 , "imaginaryPart": 6}]
    assert operations.calculateSequenceSum(lst , [0 , 2]) == {"realPart": 14 , "imaginaryPart": 13}

    lst = [{"realPart": 3, "imaginaryPart": 4}, {"realPart": 3, "imaginaryPart": 5},
           {"realPart": 8, "imaginaryPart": 4}, {"realPart": 4, "imaginaryPart": -3},
           {"realPart": -3, "imaginaryPart": -4}, {"realPart": 6, "imaginaryPart": 10},
           {"realPart": 1, "imaginaryPart": 2}, {"realPart": 6, "imaginaryPart": 6}]

    assert operations.calculateSequenceSum(lst , [3 , 4]) == {"realPart": 1 , "imaginaryPart": -7}

def test_calculateSequenceProduct():
    '''
    Test function for calculateSequenceProduct()
    '''
    lst = [{"realPart": 1 , "imaginaryPart": 1} , {"realPart": 2 , "imaginaryPart": 1} , {"realPart": 1 , "imaginaryPart": -2}]
    assert operations.calculateSequenceProduct(lst , [0 , 2]) == {"realPart": 7 , "imaginaryPart": 1}

    lst = [{"realPart": 3 , "imaginaryPart": 4} , {"realPart": 2 , "imaginaryPart": -1} , {"realPart": 1 , "imaginaryPart": 1}]

    assert operations.calculateSequenceProduct(lst , [0 , 2]) == {"realPart": 5 , "imaginaryPart": 15}

    lst = [{"realPart": 1 , "imaginaryPart": -1} , {"realPart": 3 , "imaginaryPart": 2} , {"realPart": 2 , "imaginaryPart": -3} , {"realPart": -1 , "imaginaryPart": 1}]
    assert operations.calculateSequenceProduct(lst , [0 , 3]) == {"realPart": 10 , "imaginaryPart": 24}

    lst = [{"realPart": 1, "imaginaryPart": -1}, {"realPart": 3, "imaginaryPart": 2},
           {"realPart": 2, "imaginaryPart": -3}, {"realPart": -1, "imaginaryPart": 1}]

    assert operations.calculateSequenceProduct(lst , [0 , 2]) == {"realPart": 7, "imaginaryPart": -17}

def test_sortListInverted():
    '''
    Test function for sortListInverted()
    '''
    lst = [{"realPart": 3 , "imaginaryPart": 4} , {"realPart": 2 , "imaginaryPart": -1} , {"realPart": 1 , "imaginaryPart": 1}]
    assert operations.sortListInverted(lst) == [{"realPart": 3 , "imaginaryPart": 4} , {"realPart": 1 , "imaginaryPart": 1} , {"realPart": 2 , "imaginaryPart": -1}]

    lst = [{"realPart": 1 , "imaginaryPart": -1}, {"realPart": 3 , "imaginaryPart": 2}, {"realPart": 2 , "imaginaryPart": -3}, {"realPart": -1 , "imaginaryPart": 1}]
    assert operations.sortListInverted(lst) == [{"realPart": 3 , "imaginaryPart": 2} ,  {"realPart": -1 , "imaginaryPart": 1} , {"realPart": 1 , "imaginaryPart": -1} , {"realPart": 2 , "imaginaryPart": -3}]

    lst = []
    assert operations.sortListInverted(lst) == []

def test_getRealPart():
    '''
    Test function for getRealPart()
    '''
    number = {"realPart": 2, "imaginaryPart": 4}
    assert other.getRealPart(number) == 2

    number = {"realPart": -2, "imaginaryPart": 4}
    assert other.getRealPart(number) == -2

def test_getImaginaryPart():
    '''
    Test function for getImaginaryPart()
    '''
    number = {"realPart": 2, "imaginaryPart": 4}
    assert other.getImaginaryPart(number) == 4

    number = {"realPart": 2, "imaginaryPart": -44}
    assert other.getImaginaryPart(number) == -44

def test_backupUpdate():
    '''
    Test function for backupUpdate()
    '''
    lst = [{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}]
    backup = []
    backup = undo.backupUpdate(backup, lst)
    assert backup == [[{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}]]

    lst.append({"realPart": 4, 'imaginaryPart': 4})
    backup = undo.backupUpdate(backup, lst)
    assert backup == [[{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}] , [{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 4, "imaginaryPart": 4}]]

def test_undo():
    '''
    Test function for undo()
    '''
    lst = [{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2} , {"realPart": 4, 'imaginaryPart': 4}]
    backup = [[{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}] , [{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}, {"realPart": 4, "imaginaryPart": 4}]]
    lst = undo.undo(backup, lst, [])
    assert lst == [{"realPart": 1, "imaginaryPart": 1}, {"realPart": 2, "imaginaryPart": 2}]

    lst = [{"realPart": 1, "imaginaryPart": 1}]
    lst_1 = [{"realPart": 10, "imaginaryPart": 10}]
    backup = []
    lst = undo.undo(backup, lst, lst_1)
    assert lst == [{"realPart": 10, "imaginaryPart": 10}]

def test_all():
    '''
    Runs all test functions
    '''
    test_validateIndex()
    test_validateSequenceIndex()
    test_validateOption()

    test_addNumberToList()
    test_insertNumberInList()

    test_deleteNumber()
    test_deleteSequence()
    test_replaceNumber()

    test_findNumbersInSequence()
    test_isModuleUnder10()
    test_isModule10()

    test_calculateSequenceSum()
    test_calculateSequenceProduct()
    test_sortListInverted()

    test_filterPrime()
    test_filterHigherModule()
    test_filterLowerModule()
    test_filterEqualModule()

    test_isPrime()
    test_calculateModule()
    test_getRealPart()
    test_getImaginaryPart()

    test_backupUpdate()
    test_undo()

test_all()
