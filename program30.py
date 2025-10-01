import threading
import time

def worker():
    print(f"Thread {threading.current_thread().name} is running")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} is exiting")

# (i) Create thread
t1 = threading.Thread(target=worker, name="T1")
t2 = threading.Thread(target=worker, name="T2")

t1.start()
t2.start()

# (ii) Join thread
t1.join()
t2.join()

# (iii) Equal check
if t1 == t2:
    print("Threads are equal")
else:
    print("Threads are NOT equal")

# (iv) Exit is implicit when function ends
print("Main thread exiting")
