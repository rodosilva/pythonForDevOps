
# Write a program that counts down from a given number to zero.

countdown = 11
while countdown >= 0:
    print(countdown)
    countdown -= 1

# Create a program that keeps accepting positive numbers from the user and calculates their sum until the user enters a negative number.

number = 0
result = 0

while True:
  number = int(input("Enter a positive number: "))
  
  if result == 0 and number >= 0:
      print(f"The initial number is {number}")
      result = number
      
  elif result > 0:
      result += number
      print(f"The sum is: {result}")
  elif number < 0:
      print("Negative number entered. Exiting the loop.")
      break


# Implement a simple password guessing game where the user has to guess the correct password. The user has a maximum of 3 attempts

password = "correctpassword"
attempts = 3

while attempts > 0:
    guess = input("Enter the password: ")
    
    if guess == password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
        
        if attempts == 0:
            print("Access Denied. No attempts left.")



