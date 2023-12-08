
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")


# Python code​​​​​​‌​‌​‌​​​​‌​‌​​‌‌​​‌‌​‌​‌‌ below
# Use print("messages...") to debug your solution.
import calendar

show_expected_result = False
show_hints = False

def count_days(year, month, whichday):
    countdays = 0
    cal = calendar.Calendar()
    for (x,day) in cal.itermonthdays2(year, month):
        if x != 0 and day == whichday:
            countdays += 1
    
    return countdays


today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[today.weekday()+1])