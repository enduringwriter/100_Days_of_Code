# https://www.w3resource.com/python-exercises/date-time-exercise/

import datetime

print("Current date and time: ", datetime.datetime.now())

print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

day_now = datetime.datetime.now()
print(day_now)
day_of_the_week = day_now.isoweekday()
print(day_of_the_week)
day = datetime.date.today()
print(day)
day_of_week = day.isoweekday()
print(day_of_week)

if day_of_the_week == 6:
    print("Today is Saturday!")
else:
    print("Today is not Saturday.")
