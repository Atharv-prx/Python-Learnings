import datetime

date = datetime.date(2026, 4, 27)
today = datetime.date.today()

time = datetime.time(14, 30, 45)
now = datetime.datetime.now() # Daytime twice cuz first we access datetime module then datetime class inside it

now = now.strftime("%Y-%m-%d %H:%M:%S") # Format the datetime object as a string

#Checking if a specific date and time is in the future

target_datetime = datetime.datetime(2027, 4, 27, 15, 30, 45)
current_datetime = datetime.datetime.now()
if current_datetime < target_datetime:
    print("The target date and time is in the future.")
else:
    print("The target date and time is in the past.")

print(date)
print(today)

print(time)
print(now)