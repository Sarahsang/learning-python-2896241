# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# This function counts the number of the given weekday for the
# specified year and month and returns the result
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

#note: 关于week[whichday]，是这样的：
'''这是.monthcalendar(theyear, themonth)函数返回的列表
[
    [0, 0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25, 26],
    [27, 28, 29, 30, 31, 0, 0]
]
列表的特性是，可以用列表名[行号][列号]来获取列表中的元素，这里的行号就是week，列号就是whichday
week[whichday]就是获取week列表中的第whichday个元素，如果是0，就是第一个元素，如果是1，就是第二个元素，以此类推
'''

print("--Day counter program--\n")

run = True
while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter year: ")
        year = int(yearstr)

        monthstr = input("Enter month: ")
        month = int(monthstr)

        result = countdays(year, month, day)
        print("There are " + str(result) + " of those days in the month and year specified")
        print("-----------\n")
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")

