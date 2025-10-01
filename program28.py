def simulate_grep(pattern, filename):
    try:
        with open(filename, "r") as f:
            for line_no, line in enumerate(f, start=1):
                if pattern in line:
                    print(f"{filename}:{line_no}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Run (example: searching for "hello" in test.txt)
simulate_grep("hello", "test.txt")
