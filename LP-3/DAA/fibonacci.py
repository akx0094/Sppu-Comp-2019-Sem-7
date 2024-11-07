# Non-recursive (Iterative) Fibonacci function
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Recursive Fibonacci function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example of calling both functions
n=int(input("Enter a number :"))
print(f"The {n}th Fibonacci number (iterative): {fibonacci_iterative(n)}")

# Calling the recursive function
print(f"The {n}th Fibonacci number (recursive): {fibonacci_recursive(n)}")
