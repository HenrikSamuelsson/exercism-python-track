import datetime


def add(moment):
    giga_second = 1_000_000_000
    return moment + datetime.timedelta(seconds=giga_second)
