"""
03_functions.py
Topic: Functions in Python
"""

# Basic function
def greet(name):
    return f"Hello, {name}! Welcome to Python."

print(greet("Alex"))

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print("Square of 5:", power(5))
print("Cube of 5:", power(5, 3))

# Function returning multiple values
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    return total, average, highest, lowest

nums = [10, 20, 5, 40, 15]
total, avg, high, low = get_stats(nums)
print(f"\nNumbers: {nums}")
print(f"Total: {total}, Average: {avg}, Max: {high}, Min: {low}")

# Function to check even/odd
def is_even(n):
    return n % 2 == 0

for n in range(1, 6):
    label = "even" if is_even(n) else "odd"
    print(f"{n} is {label}")

# Recursive function - factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial of 5: {factorial(5)}")
