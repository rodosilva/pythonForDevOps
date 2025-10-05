
# Write a program that checks if a user is old enough to drive (age 16 or older)

age = int(input("Enter your age: "))
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Create a program that evaluates a student's grade and prints a message based on the score.

score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Excellent Work!")
elif score >= 80:
    print("Great Job!")
elif score >= 70:
    print("Good Effort!")
elif score >= 60:
    print("You Passed.")
else:
    print("Don't give up. Try harder next time!")

# Implement a program that checks the temperature and suggests what to wear.
temperature = int(input("Enter the temperature in Celsius: "))
if temperature >= 30:
    print("It's hot outside. Wear light clothing.")
elif temperature >= 20:
    print("The weather is warm. A t-shirt should be fine.")
elif temperature >= 10:
    print("It's a bit chilly. Consider wearing a sweater.")
else:
    print("It's cold outside. Wear a coat and stay warm.")

