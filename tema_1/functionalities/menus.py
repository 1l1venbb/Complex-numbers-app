from . import addToList
from . import writer
from . import reader
from . import modifyList
from . import searchInList
from . import filtering
from . import operations
from . import validator
from . import undo

backup = []

def programStart():
    '''

    This function marks the start of the program. It asks the user to enter the complex numbers list.

    :return: List of complex numbers.
    '''

    print("Welcome to my app! It'll help you manage a list of complex numbers.")

    lst = reader.readList()
    return lst

def addMenu(lst):
    '''

    Menu for methods of adding elements to the list.

    :param lst: List of complex numbers.
    :return: Modified list of complex numbers.
    '''

    while 1:

        print("\n")
        print("Press 1 to add a number at the end of the list.")
        print("Press 2 to insert a number at your desired index.")
        print("Press 3 to go back to main menu.")
        print("\n")

        while True:
            try:
                option = int(input("Select an option: "))
                validator.validateOption(option, [1, 3])
                break
            except ValueError:
                print("Invalid input.")

        if option == 1:
            x = reader.readComplexNumber()
            lst = addToList.addNumberToList(lst , x)
            undo.backupUpdate(backup, lst)

        if option == 2:
            number = reader.readComplexNumber()
            index = reader.readNumberPosition()
            lst = addToList.insertNumberInList(lst, index, number)
            undo.backupUpdate(backup, lst)

        if option == 3:
            break

    return lst

def modifyMenu(lst):
    '''

    Menu for methods of modifying the list.

    :param lst: List of complex numbers.
    :return: Modified list of complex numbers.
    '''

    while 1:

        print("\n")
        print("Press 1 to remove a number from the list.")
        print("Press 2 to remove a sequence of numbers from the list.")
        print("Press 3 to replace all instances of a number in the list.")
        print("Press 4 to go back to main menu.")
        print("\n")

        while True:
            try:
                option = int(input("Select an option: "))
                validator.validateOption(option, [1, 4])
                break
            except ValueError:
                print("Invalid input.")

        if option == 1:
            try:
                poz = reader.readNumberPosition()
                validator.validateIndexInList(lst, poz)
                lst = modifyList.deleteNumber(lst, poz)
                undo.backupUpdate(backup, lst)
                break
            except ValueError:
                print("Invalid index or list is empty.")


        if option == 2:
            try:
                poz = reader.readSequencePosition()
                validator.validateSequenceIndex(lst, poz)
                lst = modifyList.deleteSequence(lst, poz)
                undo.backupUpdate(backup, lst)
            except ValueError:
                print("Sequence index is out of range or list is empty.")

        if option == 3:
            print("First input the old number and then the new one.")
            x = reader.readComplexNumber()
            y = reader.readComplexNumber()
            try:
                lst = modifyList.replaceNumber(lst, x, y)
                undo.backupUpdate(backup, lst)
            except ValueError:
                print("Old number not found in list")

        if option == 4:
            break

    return lst

def searchInListMenu(lst):
    '''

    Menu for methods of searching in the list.

    :param lst: List of complex numbers.
    :return: Modified list of complex numbers.
    '''
    while 1:

        print("\n")
        print("Press 1 to show the imaginary part in your desired sequence.")
        print("Press 2 to show the complex number with the module smaller than 10.")
        print("Press 3 to show the complex numbers with the module equal to 10.")
        print("Press 4 to go back to main menu.")
        print("\n")

        while True:
            try:
                option = int(input("Select an option: "))
                validator.validateOption(option, [1 , 4])
                break
            except ValueError:
                print("Invalid input.")

        if option == 1:
            try:
                poz = reader.readSequencePosition()
                validator.validateSequenceIndex(lst, poz)
                rez = searchInList.findNumbersInSequence(lst, poz)
                writer.showImaginaryNumber(rez)
            except ValueError:
                print("Sequence index is out of range or list is empty.")

        if option == 2:
            rez = searchInList.isModuleUnder10(lst)
            writer.showList(rez)

        if option == 3:
            rez = searchInList.isModule10(lst)
            if rez is not []:
                writer.showList(rez)

        if option == 4:
            break

    return lst

def operationsMenu(lst):
    '''
    Menu for methods of operations.
    :param lst: List of complex numbers.
    :return: List of complex numbers.
    '''

    while 1:
        print("\n")
        print("Press 1 to calculate the sum of a desired sequence.")
        print("Press 2 to calculate the product of a desired sequence.")
        print("Press 3 to show list in decreasing order by imaginary part.")
        print("Press 4 to go back to main menu.")
        print("\n")

        while True:
            try:
                option = int(input("Select an option: "))
                validator.validateOption(option, [1, 4])
                break
            except ValueError:
                print("Invalid input.")

        if option == 1:
            try:
                poz = reader.readSequencePosition()
                validator.validateSequenceIndex(lst , poz)
                sum = operations.calculateSequenceSum(lst, poz)
                writer.showComplexNumber(sum)
            except ValueError:
                print("Sequence index is out of poz or list is empty.")


        if option == 2:
            try:
                poz = reader.readSequencePosition()
                validator.validateSequenceIndex(lst , poz)
                product = operations.calculateSequenceProduct(lst, poz)
                writer.showComplexNumber(product)
            except ValueError:
                print("Sequence index is out of poz or list is empty.")

        if option == 3:
            rez = operations.sortListInverted(lst)
            writer.showList(rez)

        if option == 4:
            break

def filteringMenu(lst):
    '''

    Menu for methods of filtering the list.

    :param lst: List of complex numbers.
    '''
    while 1:

        print("\n")
        print("Press 1 to show the complex numbers that don't have the real part a prime number.")
        print("Press 2 to show the complex numbers that are smaller, bigger or equal to your desired module ")
        print("Press 3 to go back to main menu.")
        print("\n")

        while True:
            try:
                option = int(input("Select an option: "))
                validator.validateOption(option, [1, 3])
                break
            except ValueError:
                print("Invalid input.")

        if option == 1:
            rez = filtering.filterPrime(lst)
            writer.showList(rez)

        if option == 2:
            o = reader.readFilterOption()
            module = reader.readModule()

            if o == ">":
                rez = filtering.filterHigherModule(lst, module)
                writer.showList(rez)

            if o == "<":
                rez = filtering.filterLowerModule(lst,module)
                writer.showList(rez)

            if o == "=":
                rez = filtering.filterEqualModule(lst, module)
                writer.showList(rez)

        if option == 3:
            break

def run():

    currentOption = 1
    lst = programStart()
    original_lst = [dict(item) for item in lst]

    while currentOption in [1, 2, 3, 4, 5, 6, 7, 8]:

        print("\n")
        print("Press 1 to add numbers to the list.")
        print("Press 2 to remove or modify numbers from the list.")
        print("Press 3 to search in list.")
        print("Press 4 to make operations in list.")
        print("Press 5 to show filtered numbers from the list.")
        print("Press 6 to undo the last action (keep in mind that only adding and deleting numbers affect the list).")
        print("Press 7 to show list.")
        print("Press 8 to exit program.")
        print("\n")

        while True:
            try:
                currentOption = int(input("Enter menu number: "))
                break
            except ValueError:
                print("Invalid input.")

        if currentOption == 1:
            addMenu(lst)

        if currentOption == 2:
            modifyMenu(lst)

        if currentOption == 3:
            searchInListMenu(lst)

        if currentOption == 4:
            operationsMenu(lst)

        if currentOption == 5:
            filteringMenu(lst)

        if currentOption == 6:
            lst = undo.undo(backup, lst, original_lst)
            writer.showBackup(backup)

        if currentOption == 7:
            writer.showList(lst)

        if currentOption == 8:
            exit()