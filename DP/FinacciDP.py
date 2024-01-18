def fibonacci(n):
    fib = [0] * (n + 1)  # array to store Fibonacci numbers 
    fib[1] = 1           # Set the base case F(1) = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  # Use the recurrence relation to calculate Fibonacci numbers

    return fib[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
