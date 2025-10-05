
# Create a global variable named global_var outside any function and assign it a meaningful value, such as global_var = ?
global_var = "I am a global variable"

# Use the print() function to display the value of the variable global_var in the main script
print(global_var)

# print_global_variables(): Prints a global variable.
# modify_global_variable(): Changes the global variable using the global keyword. In the main part of your script, call both functions and print the outputs

def print_global_variable():
    print("Inside function print_global_variable:", global_var)

def modify_global_variable():
    global global_var
    global_var = "global variable modified"
    print("Inside function modify_global_variable:", global_var)

print_global_variable()
modify_global_variable()

