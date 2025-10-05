
# Write a program that prints all the numbers from 1 to 10
for i in range(1,10):
    print(i)

# Create a program that prints all the even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# Implement a program that prints numbers from 10 down to 1.
for i in range(10, 0, -1):
    print(i)

# Write a program that takes a string input from the user and prints each character on a new line.
text = "Python"
for letter in text:
    print(letter)

# Create a program that counts and prints the number of vowels in a given string.
text = "Hello, welcome to Python programming!"
count = 0
for letter in text:
    if letter.lower() in "aeiou":
        count += 1

print(f"The number of vowels in the text is: {count}")

# Implement a program that reverses a given string and prints the result
text = "Python"
reversed_text = ""
for letter in text:
    reversed_text = letter + reversed_text

print(f"The reversed string is: {reversed_text}")
