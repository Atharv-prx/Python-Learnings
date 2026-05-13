# This happens when threads access and modify same data at same time and final result becomes unpredictable
import threading
counter = 0

def increment():
    global counter
    for _ in range (1000000):
        counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter) # This should be 2000000 but sometimes it is less than that because of race condition.