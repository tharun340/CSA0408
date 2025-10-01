import threading
import queue
import time
import random

BUFFER_SIZE = 5
buffer = queue.Queue(BUFFER_SIZE)

def producer():
    for i in range(10):  # Produce 10 items
        item = i + 1
        buffer.put(item)  # Blocks if buffer is full
        print(f"Producer produced: {item}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate production time

def consumer():
    for i in range(10):  # Consume 10 items
        item = buffer.get()  # Blocks if buffer is empty
        print(f"Consumer consumed: {item}")
        buffer.task_done()
        time.sleep(random.uniform(1, 2))  # Simulate consumption time

# Create threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("All items produced and consumed.")
