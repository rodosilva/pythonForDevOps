import os

folders = input("Enter folder names:").split()

for i in folders:
    print(f"=== Listing folders: {i} ===")
    try:
      listed_files = os.listdir(i)
    except FileNotFoundError:
        print(f"Error: The folder '{i}' does not exist.")
        break
    except PermissionError:
        print(f"Error: You do not have permission to access the folder '{i}'.")
        break
    for j in listed_files:
        print(j)

