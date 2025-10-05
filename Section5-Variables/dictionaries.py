
# Define dictionaries in Python.
student = {
    "name": "Rodrigo",
    "age": 38,
    "major": "Engineer"
}

# Create a dictionary called student that includes your name, age, and major.
# Use the keys to print each corresponding value
print(student["name"])
print(student["age"])
print(student["major"])

# Create a dictionary called student, then add a gpa key and update the age
student["gpa"] = 3.8
student["age"] = 39

# Print a Line to separate the outputs
print("-----")
# Create a dictionary and iterate over its key-value pairs
for key in student:
    print(key, ":", student[key])

