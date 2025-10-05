# Function with parameters
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.") # tells Python to evaluate any expressions inside curly braces {} and insert their values into the string.

# Calling the function with arguments
greet("Rodrigo", 38)

# Function that adds
def add(a, b):
    return a + b

num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {add(num1, num2)}")

