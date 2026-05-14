# What a event actually is ?
#       - An event is a synchronization primitive that allows threads to communicate with each other by signaling when a certain condition has occurred. 
#       - It provides a way for one thread to signal one or more other threads that an event has happened, allowing them to proceed with their tasks.
#       - Event has only 2 states: True or False. Initially, it is set to False. When it is set to True, it signals that event has occurred, and any threads waiting for that event can proceed.

# 1- .set() method: This method is used to set the event to True, signaling that the event has occurred. When this method is called, any threads that are waiting for the event will be unblocked and can proceed with their tasks.
# 2- .clear() method: This method is used to reset the event to False, indicating that the event has not occurred. After calling this method, any threads that are waiting for the event will be blocked until the event is set again.
# 3- .is_set() method: This method is used to check the current state of the event. It returns True if the event is set (i.e., the event has occurred) and False if the event is not set (i.e., the event has not occurred). 
#                      This method is often used by threads to check whether they should proceed with their tasks based on the state of the event.

import threading

event = threading.Event()

print(event.is_set())

event.set()

print(event.is_set())

if event.is_set():
    print("Event is set (True), proceeding with task...")
else: 
    print("Event is not set (False), waiting for event to be set...")

event.clear()

print(event.is_set())
if event.is_set():
    print("Event is set (True), proceeding with task...")
else: 
    print("Event is not set (False), waiting for event to be set...")