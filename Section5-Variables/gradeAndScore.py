# Create a Python program that asks the user to enter their score (out of 100) and then determines the corresponding letter grade based on predefined criteria

# Get user input
grade = float(input("Please enter your score (out of 100): "))

# Greeting message
print("Welcome to the Grade Calculator!")

# Determine letter grade
if grade >= 90 and grade <= 100:
    print("Your grade is: A")
elif grade >= 80 and grade <= 89:
    print("Your grade is: B")
elif grade >= 70 and grade <= 79:
    print("Your grade is: C")
elif grade >= 60 and grade <= 69:
    print("Your grade is: D")
elif grade >= 0 and grade <= 59:
    print("Your grade is: F")
else:
    print("Invalid score. Please enter a score between 0 and 100.")

