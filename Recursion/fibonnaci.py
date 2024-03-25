# Implement a function to find the nth number in the Fibonacci sequence using recursion.
# Formula Fn = Fn − 1 + Fn − 2

def fibonacci(term):
    if term <= 0:
        raise ValueError("Invalid input. n must be a positive integer.")

    if term == 1:
        return 0
    elif term == 2:
        return 1
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)


term = int(input("Enter the term to find in the Fibonacci sequence: "))
result = fibonacci(term)
print(f"The {term}th term of the Fibonacci sequence is: {result}")