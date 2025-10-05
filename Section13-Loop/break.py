# Using break statement to exit a loop

i = 0
while True:
    print(f"Iteration {i}")
    i += 1
    # Break when i reaches 10
    if i == 5:
        print("Break the loop as i reached 5")
        break
print("Loop ended.")
