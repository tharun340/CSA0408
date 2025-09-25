import threading, queue

q = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        q.put(i)
        print(f"Produced {i}")

def consumer():
    for i in range(10):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
