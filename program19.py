import threading
import time

shared_counter = 0
lock = threading.Lock()

def increment(thread_id):
    global shared_counter
    for _ in range(5):
        with lock:  # Acquire lock
            shared_counter += 1
            print(f"Thread {thread_id} incremented counter to {shared_counter}")
        time.sleep(1)

threads = []

for i in range(2):  # Two threads
    t = threading.Thread(target=increment, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final value of counter: {shared_counter}")
