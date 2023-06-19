import datetime
import re

#checks if date matches the format yyyy-mm-dd and is valid
def approve_date(date):
    pattern = r"....-..-.."
    if not(re.match(pattern, date)):
        print("Date does not match the specified format. try again: ")
        return False
    if not( (date[:4].isdigit()) and (date[5:7].isdigit()) and (date[8:].isdigit()) ):
        print("Either year, date or month has been typed wrongly. try again")
        return False
    if (int(date[5:7])<1 and int(date[5:7])>12):
        print("Wrong value for month in date. try again")
        return False
    try:
        date = datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:]))
        p = date.strftime("%a")
    except:
        print("Invalid date. Try again")
        return False

#allows date input and ensures the date is valid
#then computes the day using datetime
while True:
    date = input("Enter todays date in the format yyyy-mm-dd: ")
    choice = approve_date(date)
    if (choice==False):
        continue
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    day = datetime.datetime(year, month, day)
    day = day.strftime("%a")
    break

#to get fare for respective days
weekdays = ["Mon","Tue","Wed","Thu","Fri"]
if day in weekdays:
    fare = 100
elif day == "Sat":
    fare = 60
else:
    fare = 80

#print the results
print("Date: ",date)
print("Day: ",day)
print("Fare: ",fare)


