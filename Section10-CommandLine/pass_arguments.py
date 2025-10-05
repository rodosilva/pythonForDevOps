import sys

# Print all command line arguments
print("All the Argument Passed:", sys.argv)

# Print the first argument (script name)
print("Script Name:", sys.argv[0])

# Print the second argument (first and Second user-provided argument)
print("First User-provided Argument:", sys.argv[1])
print("Second User-provided Argument:", sys.argv[2])
print("Third User-provided Argument:", sys.argv[3])

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "add":
    result = add(num1, num2)
    print("Addition:", result)

elif operator == "subtract":
    result = subtract(num1, num2)
    print("Subtraction:", result)

elif operator == "mult":
    result = mult(num1, num2)
    print("Multiplication:", result)

else:
    print("Unsupported Operation. Use add, subtract, or mult.")





