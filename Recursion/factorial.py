# Write a function to calculate the factorial of a non-negative integer using recursion.
# n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1


def factorial(number):
    if number < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def iterations():
    num = int(input("Enter a number to factorise : "))
    x = factorial(int(num))
    print(x)

while True:
    iterations()
    ex = input("Enter (c) to continue or (q) to exit: ")
    if ex == "q":
        break
    elif ex=="c":
        continue
    elif ex!= "c":
        print("Invalid key")
    ex = input("Enter (c) to continue or (q) to exit: ")
       