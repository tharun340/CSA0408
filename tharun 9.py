from multiprocessing import Process, Value
import time

def writer(shared_value):
    print("Writer: Writing data into shared memory...")
    shared_value.value = 1234  # write data
    time.sleep(1)

def reader(shared_value):
    time.sleep(2)  # wait for writer
    print("Reader: Data read from shared memory =", shared_value.value)

if __name__ == "__main__":
    # Create shared integer memory
    shared_value = Value('i', 0)  # 'i' means integer, initial value = 0

    p1 = Process(target=writer, args=(shared_value,))
    p2 = Process(target=reader, args=(shared_value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
