# Creating too many threads manually is inefficient.
# A Thread Pool:
#    - creates reusable worker threads
#    - assigns tasks automatically to available threads

from concurrent.futures import ThreadPoolExecutor
import time

def task(num):
    print(f"Task {num} starting")

    time.sleep(2)

    print(f"Task {num} finished")

with ThreadPoolExecutor(max_workers=3) as executor:

    for i in range(5):
        executor.submit(task, i)

# Pools creates 3 worker threads and assigns tasks to them.