def walk(steps):
    
    # Base case: If there are no more steps to take, stop the recursion
    if steps == 0:
        print("You have reached your destination.")
        return
    
    # Recursive case: Take a step and call the function again with one less step
    print("You take a step.")
    walk(steps -1)

walk(5)