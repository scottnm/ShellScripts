#!/usr/bin/env python3

from enum import Enum
import datetime
from sys import stdout

month_to_maxdays_map = [31, 28, 31,  30, 31, 30,  31, 31, 30,  31, 30, 30]

def get_maxdays_in_month(month, year):
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or (year % 400 == 0)):
        return 29
    else:
        return month_to_maxdays_map[month - 1]


def days_in_range(start_date=None, end_date=None):
    # date format = (year, month, day, dayofweek) as 1 indexed numbers
    assert start_date is None or type(start_date) is datetime.datetime
    assert end_date is None or type(end_date) is datetime.datetime

    if start_date is None:
        start_date = datetime.date.today()

    if end_date is None:
        end_date = datetime.datetime(start_date.year, 12, 31)

    day_to_start = start_date.day
    for year in range (start_date.year, end_date.year + 1):
        end_month = 13 if year != end_date.year else end_date.month + 1
        for month in range (start_date.month, end_month):
            end_day = get_maxdays_in_month(month, year) + 1 \
                    if not (year == end_date.year and month == end_date.month) else \
                    end_date.day + 1
            for day in range (day_to_start, end_day):
                yield datetime.datetime(year, month, day)
            day_to_start = 1

if __name__ == "__main__":
    for d in days_in_range():
       stdout.write(str(d) + "\n") 
