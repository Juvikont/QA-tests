import datetime

def days_since(n):
    diff = datetime.datetime.now().date() -n
    return diff.days