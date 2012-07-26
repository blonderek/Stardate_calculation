import math
from sys import exit

months = {'February':2, 'October':10, 'March':3, 'August':8, 'May':5, 'January':1, 'June':6, 'September':9, 'April':4, 'December':12, 'July':7, 'November':11}

def calc(m):
    hi = int((153*((m+1)+12*(int((14-(m+1))/12))-3)+2)/5)-int((14-(m+1))/12)*365
    lo = int((153*(m+12*(int((14-m)/12))-3)+2)/5)-int((14-m)/12)*365
    return abs(hi - lo)

def days(month=''):
    if month == '':
        month = raw_input('Which month? ')
    if month == 'e':
        exit()
    month = month.capitalize()
    try:
        m = months[month]
    except KeyError:
        month = raw_input('Invalid month. Try again. ')
        days(month)
    else:
        d = calc(m)
        print "{0} has {1} days".format(month, d)
days()
