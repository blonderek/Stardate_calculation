import math
from datetime import datetime, date, time, timedelta, tzinfo

def stardate(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second):
    
    a = int((14-month)/12)
    y = year - a
    m = month + 12 * a - 3
    C = 1721118

    sd = int(y*365.2425) + int((153*m+2)/5) + day + C + (hour/24) + (minute/1440) + (second/86400)

    l, r = str(sd).split('.')
    
    return '{}.{} {} {}'.format(l[2:], r[:2], r[2:4], r[4:6])


