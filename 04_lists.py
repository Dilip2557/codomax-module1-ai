"""
04_lists.py
Topic: Lists in Python
"""

# Creating a list
students = ["Riya", "Karan", "Meena", "Aditya"]
print("Students:", students)

# Accessing elements
print("First student:", students[0])
print("Last student:", students[-1])

# Slicing
print("First two:", students[0:2])

# Adding elements
students.append("Zoya")
print("After adding Zoya:", students)

# Removing elements
students.remove("Karan")
print("After removing Karan:", students)

# Sorting
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted numbers:", numbers)

numbers.sort(reverse=True)
print("Sorted descending:", numbers)

# List comprehension - squares of numbers 1-5
squares = [n ** 2 for n in range(1, 6)]
print("Squares:", squares)

# Filtering with list comprehension - even numbers only
evens = [n for n in range(1, 20) if n % 2 == 0]
print("Even numbers 1-20:", evens)

# Looping with index using enumerate
print("\nStudent list with index:")
for index, name in enumerate(students, start=1):
    print(f"{index}. {name}")

# Length and membership
print(f"\nTotal students: {len(students)}")
print("Is 'Riya' in the list?", "Riya" in students)
