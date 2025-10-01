import threading
import time
import random

N = 5  # number of philosophers

# Create a lock for each fork
forks = [threading.Lock() for _ in range(N)]

def philosopher(id):
    while True:
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 3))  # thinking

        # Pick up left and right forks
        left = forks[id]
        right = forks[(id + 1) % N]

        # To prevent deadlock, pick lower-numbered fork first
        first, second = (left, right) if id % 2 == 0 else (right, left)

        with first:
            with second:
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 2))  # eating
                print(f"Philosopher {id} finished eating and starts thinking again.")

# Create threads for each philosopher
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# Join threads (this will run forever)
for t in threads:
    t.join()
