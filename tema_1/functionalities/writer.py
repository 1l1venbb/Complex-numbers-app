from . import other

def showBackup(lst):
    '''
    Writes the backup list.
    :param lst: Backup list.
    '''
    print("Backup starts here")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if other.getImaginaryPart(lst[i][j]) >= 0:
                print(str(other.getRealPart(lst[i][j])) + " + " + str(other.getImaginaryPart(lst[i][j])) + "i")
            else:
                print(str(other.getRealPart(lst[i][j])) + " - " + str(abs(other.getImaginaryPart(lst[i][j]))) + "i")
        print("\n")
    print("Backup ends here")

def showList(lst):
    '''

    Writes the list of complex numbers in terminal
    :param lst: list of complex numbers
    '''
    for i in range(len(lst)):
        if other.getImaginaryPart(lst[i]) >= 0:
            print(str(other.getRealPart(lst[i])) + " + " + str(other.getImaginaryPart(lst[i])) + "i")
        else:
            print(str(other.getRealPart(lst[i])) + " - " + str(abs(other.getImaginaryPart(lst[i]))) + "i")

def showImaginaryNumber(lst):
    '''

    Writes the list of imaginary numbers in terminal

    :param lst: List of complex numbers
    '''


    for i in range(len(lst)):
        print(str(other.getImaginaryPart(lst[i])) + "i")

def showComplexNumber(number):
    '''
    Writes a complex number.
    :param number: complex number
    '''
    if other.getImaginaryPart(number) >= 0:
        print(str(other.getRealPart(number)) + " + " + str(other.getImaginaryPart(number)) + "i")
    else:
        print(str(other.getRealPart(number)) + " - " + str(abs(other.getImaginaryPart(number))) + "i")