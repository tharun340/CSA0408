# File Copy Program in Python

src = input("Enter source file name: ")
dst = input("Enter destination file name: ")

try:
    with open(src, "r") as f1:
        data = f1.read()

    with open(dst, "w") as f2:
        f2.write(data)

    print(f"File copied from {src} → {dst}")

except FileNotFoundError:
    print("Error: Source file not found!")
