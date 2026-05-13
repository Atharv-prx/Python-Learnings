# As the name says a shared variable is simply a variable used by multiple threads.

import threading

numbers = []

def add_numbers(num):
    numbers.append(num)

threads = []

for x in range (5):
    thread = threading.Thread(target = add_numbers, args = (x, ))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

print(numbers)