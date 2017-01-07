#!/usr/bin/env python3
"""This example shows how to use the RTC Click wrapper of the LetMeCreate to
obtain the current date.

It sets the date to Friday 28th October, 9:44:0. Then, it prints the current
date read from the RTC Click every second. Ctrl+C must be pressed to exit
the program.

The RTC Click must be inserted in Mikrobus 1 before running this program.
"""

from letmecreate.core import i2c
from letmecreate.click import rtc
from time import sleep

# week days
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# months
JANUARY = 0
FEBRUARY = 1
MARCH = 2
APRIL = 3
MAY = 4
JUNE = 5
JULY = 6
AUGUST = 7
SEPTEMBER = 8
OCTOBER = 9
NOVEMBER = 10
DECEMBER = 11

weekday_str = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

month_str = [
    "January",
    "Februay",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = rtc.Date()
date.second = 0
date.minute = 44
date.hour   = 9
date.weekday = FRIDAY
date.day = 28
date.month = OCTOBER
date.year = 2016

i2c.init()
rtc.init(2016)
rtc.set_date(date)

while True:
    date = rtc.get_date()
    print("{} {} {} {}, {}:{}:{}\n".format(weekday_str[date.weekday],
                                           date.day,
                                           month_str[date.month],
                                           date.year,
                                           date.hour, date.minute, date.second))
    sleep(1)

i2c_release()
