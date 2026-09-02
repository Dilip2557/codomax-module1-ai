"""
02_loops.py
Topic: Loops (for and while) in Python
"""

# for loop - print numbers 1 to 5
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# for loop over a list
fruits = ["apple", "banana", "mango", "grape"]
print("\nFruits I like:")
for fruit in fruits:
    print("-", fruit)

# while loop - countdown
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# nested loop - simple multiplication table
print("\nMultiplication table of 5:")
for i in range(1, 6):
    print(f"5 x {i} = {5 * i}")

# loop with condition (break/continue)
print("\nSkip 3, stop at 7:")
for num in range(1, 10):
    if num == 3:
        continue   # skip this iteration
    if num == 7:
        break      # stop the loop
    print(num)
