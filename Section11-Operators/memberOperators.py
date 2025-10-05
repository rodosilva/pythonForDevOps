# Review the not in operator and make note of the following
# Create a program that checks if an item is not present in a shopping list.

shopping_list = ["apples", "bananas", "oranges"]
item = input("Enter an item to check: ")
if item not in shopping_list:
    print(f"{item} is not in the shopping list.")
else:
    print(f"{item} is in the shopping list.")

# Write a program that checks if a password does not contain any forbidden characters

forbidden_chars = ['$', '%', '#', '@']
password = input("Enter your password: ")

for char in forbidden_chars:
    if char in password:
        print("Password contains forbidden characters.")
        break
else:
    print("Password is valid.")


# Create a program that recommends movies if the user’s favorite movie is not in a predefined list
import random
predefined_movies = ["Inception", "The Matrix", "Interstellar"]
all_movies = ["Inception", "The Matrix", "Interstellar", "Avatar", "Titanic", "The Godfather"]
user_favorite = input("Enter your favorite movie: ")

if user_favorite not in predefined_movies:
    recommendation = random.choice(all_movies)
    print(f"Your favorite movie is not in our list. How about watching '{recommendation}'?")




