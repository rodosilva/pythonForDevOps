# Write a Python script that imports the math module, defines a variable for the number 16, and another variable to store the factorial of 5. Use the sqrt and factorial functions, then print the results.
import math

number = 16

factorial_of_5 = math.factorial(5)
sqrt_number = math.sqrt(number)

print(f"The square root of {number} is: {sqrt_number}")
print(f"The factorial of 5 is: {factorial_of_5}")

# Write a script that generates a random float between 0 and 1, followed by a random integer within a specified range

import random
random_float = random.random()
random_integer = random.randint(1, 100)

print(f"Random float between 0 and 1: {random_float}")
print(f"Random integer between 1 and 100: {random_integer}")

# Create a script that retrieves the current date and time, formats it, and displays the result.
import datetime

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted_datetime}")

# Write a script that converts a string to uppercase and checks if it contains a specific substring.
import re

sample_string = "Hello, welcome to Python programming."
uppercase_string = sample_string.upper()

contains_python = re.search(r"PYTHON", uppercase_string)
if contains_python:
    print("The string contains 'PYTHON'.")

# This would be another way without regex
contains_python_method2 = "PYTHON" in uppercase_string
if contains_python_method2:
    print("The string contains 'PYTHON' (method 2).")