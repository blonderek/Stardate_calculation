import math

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

def calc(m):
    hi = int((153*((m+1)+12*(int((14-(m+1))/12))-3)+2)/5)-int((14-(m+1))/12)*365
    lo = int((153*(m+12*(int((14-m)/12))-3)+2)/5)-int((14-m)/12)*365
    return abs(hi - lo)

def days(month=''):
    if month == '':
        month = raw_input("Which month? Type 'all' to see a list. ")
    month = month.capitalize()
    if month == 'All':
        for k, n in months.iteritems():
            d = calc(k)
            print "{0} has {1} days".format(n, d)
   
    elif month in months.values():
        for k, n in months.iteritems():
            if n == month:
                d = calc(k)
                print "{0} has {1} days".format(n, d)
                break
    else:
        month = raw_input('Invalid month. Try again. ')
        days(month)

days()
