import threading
import time
import random

buffer = []
buffer_size = 5

empty = threading.Semaphore(buffer_size)  # initially buffer_size empty slots
full = threading.Semaphore(0)             # initially no full slots
mutex = threading.Lock()

def producer():
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer produced: {item}")
        mutex.release()
        full.release()
        time.sleep(1)

def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(2)

# Run
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()
