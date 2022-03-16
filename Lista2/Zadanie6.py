
def DayToEnd1():
    import datetime

    today = datetime.date.today()
    year = today.year
    date_end_year = datetime.date(year, 12, 31)
    delta = date_end_year - today
    print(f"{delta.days} days")
    return


def DayToEnd2():
    import datetime

    today = datetime.datetime.today()
    year = today.year
    date_end_year = datetime.datetime(year, 12, 31)
    delta = date_end_year - today
    print(f"{delta}")
    return


DayToEnd1()
DayToEnd2()
