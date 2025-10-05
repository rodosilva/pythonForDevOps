import math
import os
import sys

# Calculate the square root of a number
sqrt_value = math.sqrt(16)
print(f"The square root of 16 is: {sqrt_value}")

# Get the current working directory
current_directory = os.getcwd()
print(f"The current working directory is: {current_directory}")

# List files in the current directory
files = os.listdir(current_directory)
print(f"Files in the current directory: {files}")

# List current Python version and command line arguments
python_version = sys.version
command_line_args = sys.argv
print(f"Python version: {python_version}")
print(f"Command line arguments: {command_line_args}")


