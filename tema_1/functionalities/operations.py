from . import other
from .other import getImaginaryPart


def calculateSequenceSum(lst, poz):
    '''
    Calculates the sum of all complex numbers in sequence.
    :param lst: List of complex numbers.
    :param poz: Sequence start and end indexes.
    :return: Sum
    '''
    sum = {"realPart" : 0 , "imaginaryPart" : 0}
    i = poz[0]

    while i <= poz[1]:
        sum["realPart"] += other.getRealPart(lst[i])
        sum["imaginaryPart"] += other.getImaginaryPart(lst[i])
        i+=1

    return sum

def calculateSequenceProduct(lst, poz):
    '''
    Calculates the product of all complex numbers in sequence.
    :param lst: List of complex numbers.
    :param poz: Sequence start and end indexes.
    :return: Product
    '''
    prod = {"realPart" : other.getRealPart(lst[poz[0]]) , "imaginaryPart" : getImaginaryPart(lst[poz[0]])}

    for i in range(poz[0] + 1, poz[1] + 1):
        real =  prod["realPart"] * other.getRealPart(lst[i]) - prod["imaginaryPart"] * other.getImaginaryPart(lst[i])
        imaginary = prod["imaginaryPart"] * other.getRealPart(lst[i]) + prod["realPart"] * other.getImaginaryPart(lst[i])

        prod["realPart"] = real
        prod["imaginaryPart"] = imaginary


    return prod

def sortListInverted(lst):
    '''
    Sorts the list in inverted order by the imaginary part pf the complex numbers.
    :param lst: List of complex numbers.
    :return: Ordered list of complex numbers.
    '''
    rez = lst
    rez.sort(reverse=True , key = lambda x : x["imaginaryPart"])
    return rez