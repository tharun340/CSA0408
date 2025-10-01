import os
import fcntl
import stat

# ----------------- fcntl demo -----------------
fd = os.open("test.txt", os.O_RDWR | os.O_CREAT)

print("File 'test.txt' opened successfully.")

# Locking the file using fcntl
try:
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  # exclusive lock
    print("File locked successfully using fcntl.")
except BlockingIOError:
    print("File is already locked.")

# ----------------- lseek demo -----------------
pos = os.lseek(fd, 0, os.SEEK_END)
print(f"Moved file pointer to end using lseek. Position = {pos}")

# ----------------- stat demo -----------------
fileStat = os.stat("test.txt")
print(f"File Size: {fileStat.st_size} bytes")
print(f"File Permissions: {oct(fileStat.st_mode & 0o777)}")
print(f"Number of Links: {fileStat.st_nlink}")

# ----------------- opendir and readdir demo -----------------
print("\nFiles in current directory:")
with os.scandir(".") as entries:
    for entry in entries:
        print(" ", entry.name)

# Unlock file
fcntl.flock(fd, fcntl.LOCK_UN)
print("\nFile unlocked successfully.")

os.close(fd)
