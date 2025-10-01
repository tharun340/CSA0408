import threading
import time

# Function executed by thread 1
def task1():
    for i in range(1, 6):
        print(f"Thread 1: Count {i}")
        time.sleep(1)  # simulate work

# Function executed by thread 2
def task2():
    for i in range(1, 6):
        print(f"Thread 2: Count {i}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Main: Both threads finished execution.")
