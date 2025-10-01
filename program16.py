import pickle
import os

FILENAME = "employee.dat"

def load_employees():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            return pickle.load(f)
    return []

def save_employees(employees):
    with open(FILENAME, "wb") as f:
        pickle.dump(employees, f)

def add_employee(employees):
    e_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    employees.append({"id": e_id, "name": name, "salary": salary})
    save_employees(employees)
    print("Employee added successfully.")

def display_employees(employees):
    if not employees:
        print("No employee records found.")
        return
    print("\nID\tName\tSalary")
    for e in employees:
        print(f"{e['id']}\t{e['name']}\t{e['salary']:.2f}")

def search_employee(employees):
    e_id = int(input("Enter Employee ID to search: "))
    for e in employees:
        if e['id'] == e_id:
            print(f"Employee Found: ID={e['id']}, Name={e['name']}, Salary={e['salary']:.2f}")
            return
    print("Employee not found!")

def modify_employee(employees):
    e_id = int(input("Enter Employee ID to modify: "))
    for e in employees:
        if e['id'] == e_id:
            e['name'] = input("Enter new Name: ")
            e['salary'] = float(input("Enter new Salary: "))
            save_employees(employees)
            print("Employee record updated successfully.")
            return
    print("Employee not found!")

def main():
    employees = load_employees()

    while True:
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Modify Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            modify_employee(employees)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
