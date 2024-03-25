def sumofDigit(number):
    assert number >0 and int(number) ,"Number must be positive and integer"
    if number< 10:
        return number
    else:
     return number%10 + sumofDigit(int(number/10))

input=int(input("Enter a number: "))
x=sumofDigit(input)
print(x)