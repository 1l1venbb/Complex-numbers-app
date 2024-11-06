from . import validator

def readComplexNumber():
    '''

    Reads a complex number and returns it.

    :return: Complex number (list).
    '''
    while True:
        try:
            x = int(input("Input the real part of the number:"))
            break
        except ValueError:
            print("Invalid input")

    while True:
        try:
            y = int(input("Input the imaginary part of the number:"))
            break
        except ValueError:
            print("Invalid input")

    dic = {"realPart" : x, "imaginaryPart" : y}

    return dic

def readNumberPosition():
    '''

    Reads the index of a number and returns it.

    :return: Index of a number (int).
    '''

    while True:
        try:
            poz = int(input("Input the index of your number:"))
            validator.validateIndex(poz)
            break
        except ValueError:
            print("Invalid index")

    return poz

def readSequencePosition():
    '''

    Reads the starting and ending indexes of a sequence and returns it.

    :return: List with 1 pair of starting and ending indexes.
    '''

    while True:
        try:
            start = int(input("Input the start of the sequence:"))
            validator.validateIndex(start)
            break
        except ValueError:
            print("Invalid input")

    while True:
        try:
            end = int(input("Input the end of the sequence:"))
            validator.validateIndex(end)
            break
        except ValueError:
            print("Invalid input")

    return [start , end]

def readList():
    '''

    Reads a list of complex numbers and returns it.

    :return: List of complex numbers.
    '''
    while True:
        try:
            n = int(input("Input the length of your list:"))
            if n < 1:
                raise ValueError("Invalid input")
            break
        except ValueError:
            print("Invalid input")



    lst = []

    for i in range(n):

        x = readComplexNumber()
        lst.append(x)

    return lst

def readFilterOption():

    option = 'a'

    while option not in ['<' , '>' , '=']:
        try:
            option = str(input("Input the option to filter (choose between < , > or =):"))
            break
        except ValueError:
            print("Invalid input")

        print("Invalid input")

    return option

def readModule():

    while True:
        try:
            n = int(input("Input the value of your desire module:"))
            if n >= 0:
                break
        except ValueError:
            print("Invalid input")

    return n

def readCommands():

    rez = input("Write your commands (add <num1> <num2>, delete <numIndex>, sum <seqIndex1> <seqIndex2>, undo, show, stop):")
    return rez
