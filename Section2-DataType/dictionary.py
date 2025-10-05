
# Create a dictionary with three key-value pairs

dic = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Original Dictionary: ", dic)

# Access a value using a key
print("Name: ", dic["name"])

# Add a new key-value pair to the dictionary
dic["profession"] = "Engineer"

# Update the value of an existing key
dic["age"] = 26

# Delete a key-value pair from the dictionary
dic.pop("city")
print("Modified Dictionary: ", dic)