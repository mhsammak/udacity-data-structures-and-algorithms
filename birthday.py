def is_leapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month, is_leapyear=False):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28 if not is_leapyear else 29
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30


def age(year_from, month_from, day_from, year_to, month_to, day_to):
    days = 0
    if year_from == year_to:
        if month_from == month_to:
            days += day_to - day_from
            return days
        else:
            days += days_in_month(month_from, is_leapyear(year_from)) - day_from
            month_from += 1
            while month_from < month_to:
                days += days_in_month(month_from, is_leapyear(year_from))
            days += day_to
            return days
    else:
        days += days_in_month(month_from, is_leapyear(year_from)) - day_from
        month_from += 1
        while month_from < 13:
            days += days_in_month(month_from, is_leapyear(year_from))
            month_from += 1
        year_from += 1
        while year_from < year_to:
            days += 366 if is_leapyear(year_from) else 365
            year_from += 1
        month = 1
        while month < month_to:
            days += days_in_month(month, is_leapyear(year_from))
            month += 1
        days += day_to
        return days


if __name__ == '__main__':
    print(age(1992, 10, 21, 2020, 9, 2))