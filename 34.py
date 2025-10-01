def sequential_allocation(start, length, size=50):
    disk = [0] * size
    for i in range(start, start + length):
        if disk[i] == 1:
            print(f"Block {i} already allocated!")
            return
    for i in range(start, start + length):
        disk[i] = 1
    print(f"File allocated from block {start} to {start + length - 1}")

start = int(input("Enter starting block: "))
length = int(input("Enter length of file: "))
sequential_allocation(start, length)
