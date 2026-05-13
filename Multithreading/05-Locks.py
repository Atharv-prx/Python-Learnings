# A Lock prevents multiple threads from accessing critical code simultaneously.

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for i in range (1000000):
        with lock: # This will acquire the lock before executing the block and release it after the block is executed.
            counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter) # This should always be 2000000 because of the lock.