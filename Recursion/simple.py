# Demonstrating LIFO

def printout_1():
    printout_2()
    print("I am the first function call")


def printout_2():
    printout_3()
    print("I am the second function call")


def printout_3():
    printout_4()
    print("I am the third function call")


def printout_4():
    print("I am the fourth function call")


printout_1()