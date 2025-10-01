directory = []

def create_file():
    filename = input("Enter file name to create: ")
    if filename in directory:
        print("File already exists!")
    else:
        directory.append(filename)
        print("File created successfully.")

def delete_file():
    filename = input("Enter file name to delete: ")
    if filename in directory:
        directory.remove(filename)
        print("File deleted successfully.")
    else:
        print("File not found!")

def search_file():
    filename = input("Enter file name to search: ")
    if filename in directory:
        print(f"File found at position {directory.index(filename)+1}")
    else:
        print("File not found!")

def display_files():
    if not directory:
        print("Directory is empty.")
    else:
        print("Files in directory:")
        for f in directory:
            print(f)

while True:
    print("\n--- Single Level Directory ---")
    print("1. Create File")
    print("2. Delete File")
    print("3. Search File")
    print("4. Display Files")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_file()
    elif choice == '2':
        delete_file()
    elif choice == '3':
        search_file()
    elif choice == '4':
        display_files()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
