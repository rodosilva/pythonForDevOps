# Import user-defined module
import mymodule

# Use functions and variable from the user-defined module
name = "Alice"
greeting = mymodule.greet(name)
print(greeting)

# Use the add function from mymodule
result = mymodule.add(10, 20)
print(f"The sum of 10 and 20 is: {result}")

# Access the variable from mymodule
print(f"The value of my_variable from mymodule is: {mymodule.my_variable}")
