# Return multiple values

def get_details():
    name = "Jack"
    age = 30
    city = "New York"
    return name, age, city

details = get_details()
print(details)  # Output: ('Jack', 30, 'New York')

def check_even(number):
    if number % 2 == 0:
        return True
    return False

result = check_even(4)
print("Is it event?", result)  # Output: True