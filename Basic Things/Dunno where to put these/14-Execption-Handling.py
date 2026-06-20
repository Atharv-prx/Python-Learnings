# exception = An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1/number)

except ZeroDivisionError:
    print("Can't divide by 0 lmao")

except ValueError:
    print("Enter only number ")

except Exception:
    print("Something went wrong")

finally: #used basically in file handling
    print("Do some cleanup here")