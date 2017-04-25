#!/usr/bin/env python3

# pylint: disable=invalid-name
# pylint: disable=missing-docstring

from datetime import date
import sys

month_to_maxdays_map = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]

def get_maxdays_in_month(month, year):
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or (year % 400 == 0)):
        return 29
    return month_to_maxdays_map[month - 1]


def days_in_range(start_date=None, end_date=None):
    # date format = (year, month, day, dayofweek) as 1 indexed numbers
    assert start_date is None or isinstance(start_date, date)
    assert end_date is None or isinstance(end_date, date)

    if start_date is None:
        start_date = date.today()

    if end_date is None:
        end_date = date(start_date.year, 12, 31)

    day_to_start = start_date.day
    for year in range(start_date.year, end_date.year + 1):
        end_month = 13 if year != end_date.year else end_date.month + 1
        for month in range(start_date.month, end_month):
            end_day = get_maxdays_in_month(month, year) + 1 \
                    if not (year == end_date.year and month == end_date.month) else \
                    end_date.day + 1
            for day in range(day_to_start, end_day):
                yield date(year, month, day)
            day_to_start = 1

def write_base_log(out):
    line_fmt = "{}, {}\n"
    out.write(line_fmt.format("Date", "Workout"))
    day_gen = (d for d in days_in_range(date(2017, 1, 19), date.today())
               if d.weekday() == 1 or d.weekday() == 3)
    for day in day_gen:
        out.write(line_fmt.format(str(day), "Circuit"))

if __name__ == "__main__":
    with open("workout_log.csv", "w") as f:
        write_base_log(f)
