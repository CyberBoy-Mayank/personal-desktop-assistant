# Modules
from datetime import datetime, date
from holidays import India
from speak import say
from calendar import day_name

strTime = datetime.now().strftime("%H:%M:%S")
now = datetime.now()
month_name = now.month
d_name = now.day
year_name = now.year
mName = datetime.strptime(str(month_name), "%m")
ordinalNames = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
                '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
dn = ordinalNames[d_name - 1]
mn = mName.strftime("%B")  # %B = full name of month & %b = short name of the month.


def currentTime():
    """Get current time."""
    return strTime


def todayDate():
    """Get today's date."""
    tDate = f"{mn} {dn} {year_name}"
    return tDate


def whatToday():
    """Get today's date and holiday."""
    today = date.today()
    ind_holidays = India(years=year_name)
    if ind_holidays.get(today) is None:
        return say(txt=f"Today is the {mn} {dn} {year_name} and there is no holiday today.")
    else:
        return say(txt=f"Today is {mn} {dn} {year_name} and today is {ind_holidays.get(today)}.")


def todayDayName():
    """Get today's day name."""
    t = date.today()
    named = day_name[t.weekday()]
    return say(txt=f"Sir! Today is {named}.")


def todayHoliday():
    """Get today's holiday/s."""
    today = date.today()
    ind_holidays = India(years=year_name)
    if ind_holidays.get(today):
        say(txt=f"Today is {ind_holidays.get(today)}.")
    else:
        return say(txt="Sir! There is no holiday today.")


def allHoliday():
    """Get all holidays in this year."""
    ind_holidays = India(years=year_name)
    for Date, occasion in ind_holidays.items():
        say(txt=f"{Date} : {occasion}.")
    return say(txt="These are all holidays this year.")


def timeDateCombine(query: str):
    """For say date and time."""
    if query == "get time":
        return say(txt=f"Sir! The current time is \t\t\t{currentTime()}")
    elif query == "get date":
        return say(txt=f"Today is {todayDate()}.")
