# Write a program that allows the user to input their favorite foods until they decide to stop (e.g., by entering "done"). The program should then display the complete list of favorite foods


favorite_foods = []

while True:
    food = input("Enter your favorite food (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    favorite_foods.append(food)

print("Your favorite foods are:")
for food in favorite_foods:
    print(f"- {food}")

# Create a program that starts with a predefined list of items (e.g., shopping list). Allow the user to remove an item by name and then display the updated list.

shopping_list = ["apples", "bananas", "carrots", "dates"]
print("Current shopping list:", shopping_list)
item_to_remove = input("Enter an item to remove from the shopping list: ")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print("Updated shopping list:", shopping_list)
else:
    print(f"{item_to_remove} is not in the shopping list.")

# Implement a program that takes user input to create a list of numbers and then counts how many numbers were entered.

numbers = (input("Enter some numbers:")).split()
how_many = len(numbers)
print(f"You entered {how_many} numbers.")

