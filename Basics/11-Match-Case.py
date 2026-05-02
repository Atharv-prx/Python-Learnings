#Similar to switch in c++ 

#Example-1
def day_of_week(x):
    match x:
        case 1: 
            return "It's Sunday"
        case 2: 
            return "It's Monday"       
        case 3: 
            return "It's Tuesday"            
        case 4: 
            return "It's Wednesday"
        case 5: 
            return "It's Thursday"
        case 6: 
            return "It's Friday"
        case 7: 
            return "It's Saturday"
        case _:
            return "Not a valid day"

print(day_of_week(2))

#Example-2

def is_weekend(y):
    match y:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
print(is_weekend("Saturday"))
