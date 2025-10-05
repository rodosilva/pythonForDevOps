
# Write a function that checks if a person is eligible for a senior citizen discount. A person qualifies if they are either over 65 years old or if they are a registered member of a senior program.

age = int(input("Enter your age: "))
is_member = bool(input("Are you member of the senior program? (True or False):"))

if age > 65 or is_member:
    print("You are eligible for the senior citizen discount.")
else:
    print("You are not eligible for the senior citizen discount.")

# Create a program that checks if a student has passed an exam. A student passes if they score at least 50 in Math and at least 50 in Science.

math_score = int(input("Enter your Math score: "))
science_score = int(input("Enter your Science score: "))

if math_score >= 50 and science_score >= 50:
    print("You have passed the exam.")
else:
    print("You have not passed the exam.")

# Create a program that checks if a user has access to a restricted area. The user must either be an admin or have a valid access key.

admin = "jack"
passw = "password"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == admin or password == passw:
    print("Access granted.")
else:
    print("Access denied.")


