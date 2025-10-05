
# Write a program that defines a list of fruits and prints each fruit on a new line.
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Create a program that calculates the sum of numbers in a given list

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"The sum of the numbers is: {total}")

# Implement a program that counts the number of vowels in a given string.
text = "Hello, welcome to Python programming!"
count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count += 1

print(f"The number of vowels in the text is: {count}")
