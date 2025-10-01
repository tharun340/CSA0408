directories = {}  # key: directory name, value: list of files

def create_directory():
    dir_name = input("Enter directory name: ")
    if dir_name in directories:
        print("Directory already exists!")
    else:
        directories[dir_name] = []
        print("Directory created successfully.")

def create_file():
    dir_name = input("Enter directory name to create file in: ")
    if dir_name not in directories:
        print("Directory not found!")
        return
    file_name = input("Enter file name to create: ")
    if file_name in directories[dir_name]:
        print("File already exists!")
    else:
        directories[dir_name].append(file_name)
        print("File created successfully.")

def delete_file():
    dir_name = input("Enter directory name to delete file from: ")
    if dir_name not in directories:
        print("Directory not found!")
        return
    file_name = input("Enter file name to delete: ")
    if file_name in directories[dir_name]:
        directories[dir_name].remove(file_name)
        print("File deleted successfully.")
    else:
        print("File not found!")

def search_file():
    dir_name = input("Enter directory name to search in: ")
    if dir_name not in directories:
        print("Directory not found!")
        return
    file_name = input("Enter file name to search: ")
    if file_name in directories[dir_name]:
        print(f"File found at position {directories[dir_name].index(file_name)+1} in directory {dir_name}")
    else:
        print("File not found!")

def display_files():
    dir_name = input("Enter directory name to display files: ")
    if dir_name not in directories:
        print("Directory not found!")
        return
    if not directories[dir_name]:
        print("No files in directory.")
    else:
        print(f"Files in directory {dir_name}:")
        for f in directories[dir_name]:
            print(f)

while True:
    print("\n--- Two Level Directory ---")
    print("1. Create Directory")
    print("2. Create File")
    print("3. Delete File")
    print("4. Search File")
    print("5. Display Files in Directory")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_directory()
    elif choice == '2':
        create_file()
    elif choice == '3':
        delete_file()
    elif choice == '4':
        search_file()
    elif choice == '5':
        display_files()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")
