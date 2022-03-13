
# from distutils.log import error
# from doctest import debug


# def oddOrEven(value):
#     if isdevideBy2(value):
#         return "Even"
#     return "Odd"


# def isdevideBy2(value):
#     return value % 2 == 0


# while True:
#     print("enter any number positive for check if even or odd ,enter -1 for exit")
#     try:
#         enterdValue = int(input())
#         if enterdValue == -1:
#             break
#         elif enterdValue < -1:
#             raise Exception("Error")
#         print(oddOrEven(enterdValue))

#     except:
#         debug
#         print("u input a wrong value not number or minus")
#         break
# ***************************************************************

def firstTriangle(rowNumber):
    for row in reversed(range(1,rowNumber+1)):
        print("*"*(row))
    print("--------------------------------")


def secondTriangle(rowNumber):

    for row in range(1,rowNumber+1):
        print("*"*(row))

    print("--------------------------------")


def thirdTriangle(rowNumber):

    for row in reversed(range( 1,rowNumber+1)):
        print(" "*(rowNumber-(row)), end="")
        print("*"*(row))
    print("--------------------------------")

def fourthTriangle(rowNumber):

    for row in range(1,rowNumber+1):
        print(" "*(rowNumber-(row)), end="")
        print("*"*(row))
    print("--------------------------------")



print("enter any number from 1 to 9")
try:
    rowNumber = int(input())
    if rowNumber > 0 and rowNumber < 10:
        firstTriangle(rowNumber)
        secondTriangle(rowNumber)
        thirdTriangle(rowNumber)
        fourthTriangle(rowNumber)
    else:
        print("u entered worng ")
except:
    print("u entered a wrong input not anumber")
