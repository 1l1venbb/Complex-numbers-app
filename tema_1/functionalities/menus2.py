from . import reader
from . import addToList
from . import undo
from . import validator
from . import modifyList
from . import operations
from . import writer

backup = []

def programStart():
    '''

    This function marks the start of the program. It asks the user to enter the complex numbers list.

    :return: List of complex numbers.
    '''

    print("Welcome to my app! It'll help you manage a list of complex numbers.")

    lst = reader.readList()
    return lst

def run():
    '''
    Runs the program in multiple commands mode.
    '''
    lst = programStart()
    original_lst = lst.copy()
    while True:

        comm = reader.readCommands()
        commands = comm.split()


        for i in range(len(commands)):
            if commands[i] == "add":
                try:
                    x = {"realPart": int(commands[i + 1]) , "imaginaryPart": int(commands[i + 2])}
                    lst = addToList.addNumberToList(lst , x)
                    undo.backupUpdate(backup, lst)
                except ValueError:
                    print("Invalid input")

            if commands[i] == "delete":
                while True:
                    try:
                        poz = int(commands[i + 1])
                        validator.validateIndexInList(lst, poz)
                        lst = modifyList.deleteNumber(lst, poz)
                        undo.backupUpdate(backup, lst)
                        break
                    except ValueError:
                        print("Invalid index or list is empty.")
                        break

            if commands[i] == "sum":
                try:
                    poz = [int(commands[i + 1]) , int(commands[i + 2])]
                    validator.validateSequenceIndex(lst , poz)
                    sum = operations.calculateSequenceSum(lst, poz)
                    writer.showComplexNumber(sum)
                except ValueError:
                    print("Sequence index is out of poz or list is empty.")

            if commands[i] == "undo":
                lst = undo.undo(backup, lst, original_lst)
                #writer.showBackup(backup)

            if commands[i] == "show":
                writer.showList(lst)

            if commands[i] == "stop":
                exit()


#undo add 4 5 add 3 4 add 20 undo undo sum 0 1 sum 1 2