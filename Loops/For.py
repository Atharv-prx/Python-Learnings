# Execute a block of code a number of times
# Can iterate over a range, string, sequence, etc.

# Basic syntax = for x in range(1, 11, 2):  
#                    print(x)              ----> Prints 1 to 11 with interval of 2

# ---------------- CONTINUE ----------------

for x in range(1, 10):
   if x == 5:
       continue
   else:
       print(x)

# ---------------- BREAK ----------------

for x in range(1, 10):
   if x == 5:
       break
   else:
       print(x)