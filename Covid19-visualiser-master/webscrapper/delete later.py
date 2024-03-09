import _datetime
import datetime
import time
import sys
import pytz
from pytz import timezone
print(datetime.__file__)
print(pytz.timezone('Asia/Kolkata'))
print(datetime.now(pytz.timezone('Asia/Kolkata')))

def check():
    flag = int(0)
    dates = []

    a = datetime.datetime.now()
    current_time = str(a.strftime("%H"))
    today_date = str(datetime.date.today())
    print(current_time)
    if current_time == '09':
        pass
    else:
        flag = 1
    return flag


def format():
    flag = check()
    if flag == 0:
        print("updated")
    else:
        print("already exist")

    return None


format()
