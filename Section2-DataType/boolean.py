
# Prompt the user to enter their age and whether they have a valid driver’s license
age = int(input("Enter your age: "))
license = input("Do you have a valid driver's license? (yes/no): ").strip().lower()

# Convert the age input to an integer and the license input to a Boolean value (assume "Yes" is True and "No" is False)
if license == 'yes':
    license = True,
else:
    license = False

print("Your age is:", age)
print("Do you have a valid driver's license?", license)

# If the user is at least 18 years old and has a valid driver’s license, print "You can drive."
# If the user is under 18, print "You are too young to drive."
# If the user is 18 or older but does not have a valid driver’s license, print "You cannot drive without a license."

if age >= 18 and license:
    print("You can drive.")
elif age < 18:
    print("You are too young to drive.")
elif age >= 18 and not license:
    print("You cannot drive without a license.")

# Create a Boolean variable can_drive that is True if both conditions (age and license) are satisfied, and False otherwise. Print the value of can_drive

if age >= 18 and license:
    can_drive = True
else:
    can_drive = False

print("Can you drive?", can_drive)

# Ask the user if they want to drive today (Yes/No). Convert this input to a Boolean value.
# If they can drive and want to drive today, print "Great! Have a safe drive!" Otherwise, print "Okay, maybe next time."

want_to_drive = input("Do you want to drive today? (yes/no): ").strip().lower()

if want_to_drive == 'yes':
    want_to_drive = True
else:
    want_to_drive = False

if can_drive and want_to_drive:
    print("Great! Have a safe drive!")
else:
    print("Okay, maybe next time.")

