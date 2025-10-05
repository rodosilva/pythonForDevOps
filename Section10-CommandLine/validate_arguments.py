import sys

# Print all command line arguments
print("All the Argument Passed:", sys.argv)

# Validate if arguments are passed
if len(sys.argv) > 1:
    first_argument = sys.argv[1]
    print("First Argument:", first_argument)
else:
    print("No arguments were passed.")


