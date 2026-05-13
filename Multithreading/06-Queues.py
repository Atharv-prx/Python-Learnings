# Queues are the BEST way for threads to communicate safely.
# Instead of sharing variables directly:
#    - one thread puts data into queue
#    - another thread reads from queue
# Python queue is already thread-safe.

import threading
import queue
import time

q = queue.Queue() # This will create a thread-safe queue.

def producer():
    for i in range (5):
        print(f"Produced {i}")
        q.put(i) # This will put an item into the queue. If the queue is full, it will block until a free slot is available.
        time.sleep(1) # This is just to simulate some delay in producing items. In real-world applications, this could be time taken to fetch data from an API, read from a file, etc.

def consumer():
    while True:
        item = q.get() # This will block until an item is available in the queue.
        print(f"Consumed {item}")
        q.task_done() # This will indicate that a formerly enqueued task is complete.

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)

producer_thread.start() # This will start the producer thread which will produce items and put them in the queue.
consumer_thread.start() # This will start the consumer thread which will consume items from the queue. Since it's a daemon thread, it will automatically exit when the main program exits.

producer_thread.join() # This will wait for the producer thread to finish producing items. 
                       # Once the producer thread is done, we can call q.join() to wait until all items in the queue have been processed by the consumer thread.

q.join()

print("All tasks completed")

# Daemon threads run in the background.
# They will automatically exit when the main program exits.
# Usefull for - background monitoring, autosave system, notification, logging etc.