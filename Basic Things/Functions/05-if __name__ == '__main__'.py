# We use if _name_ == '_main_' so that if we need our file do not run automatically when we import our file to another program 

# Basic Str
# def main():
#     #Program goes here 
#     pass

# if _name_ == '_main_':
#     main()

#-->Wrong use
print("This always runs")

def main():
    print("Inside main")

if __name__ == "__main__":
    main()
#This will still output "This always runs" if we import this to other work 

#-->Correction
def main():
    print("Inside main")

if __name__ == "__main__":
    main()
#Now this will not automatically run when we import this to any other program