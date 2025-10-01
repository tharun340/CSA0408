from multiprocessing import Process, Queue
import time

def writer(q):
    msg = "Hello from Writer (child process)"
    print("Writer: Sending message...")
    q.put(msg)  # send message to queue
    time.sleep(1)

def reader(q):
    time.sleep(2)  # wait for writer
    msg = q.get()  # receive message
    print("Reader: Message received =", msg)

if __name__ == "__main__":
    q = Queue()  # create message queue

    p1 = Process(target=writer, args=(q,))
    p2 = Process(target=reader, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
