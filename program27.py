import os

def simulate_ls(path="."):
    print(f"Listing files in directory: {path}\n")
    for entry in os.listdir(path):
        print(entry)

# Run
simulate_ls(".")
