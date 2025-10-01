import os

filename = "sample.txt"

# ---------- Create and Write ----------
with open(filename, "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("File Management Operations in Python.\n")
print("File created and written successfully.")

# ---------- Read ----------
with open(filename, "r") as f:
    content = f.read()
print("\nReading file contents:")
print(content)

# ---------- Append ----------
with open(filename, "a") as f:
    f.write("Appending a new line to the file.\n")
print("Data appended successfully.")

# ---------- Read Again ----------
with open(filename, "r") as f:
    content = f.read()
print("\nFile contents after append:")
print(content)

# ---------- File Information ----------
if os.path.exists(filename):
    file_info = os.stat(filename)
    print("\nFile Information:")
    print(f"Size: {file_info.st_size} bytes")
    print(f"Permissions: {oct(file_info.st_mode & 0o777)}")
    print(f"Last Modified: {file_info.st_mtime}")

# ---------- Delete ----------
os.remove(filename)
print(f"\nFile '{filename}' deleted successfully.")
