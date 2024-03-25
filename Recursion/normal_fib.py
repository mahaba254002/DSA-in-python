def fibonacci(term):
    if term <= 0:
        raise ValueError("Invalid input. n must be a positive integer.")
    
    if term in [1,2]:
        return 1

    fib_previous = 1
    fib_current = 1
    for _ in range(3, term + 1):
        fib_next = fib_previous + fib_current
        fib_previous = fib_current
        fib_current = fib_next
    
    return fib_current

term = 2
result = fibonacci(term)
print(f"The {term}th term of the Fibonacci sequence is: {result}")
