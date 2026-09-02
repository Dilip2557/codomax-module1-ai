"""
01_variables.py
Topic: Variables and Data Types in Python
"""

# Variables store data. Python figures out the type automatically.
name = "Alex"          # string
age = 21                # integer
height = 5.9             # float
is_student = True        # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)

# Check the type of a variable
print(type(name), type(age), type(height), type(is_student))

# Basic arithmetic
a = 10
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# f-strings for clean formatting
print(f"{name} is {age} years old and {height} ft tall.")
