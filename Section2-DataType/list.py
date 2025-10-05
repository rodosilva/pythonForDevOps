
# Create a list of 5 integers.
l = [1,2,3,4,5]
print("Original List: ",l)
# Add a new element to the list.
l.append(6)

# Remove the third element from the list.
l.remove(l[2])
print(l)
l.pop(3)
print(l)

# Update the value of the second element.
l[1] = 20
print("List after update: ",l)

# Print the list and its length.
print("Final List: ",l)
print("Length of the list: ", len(l))

