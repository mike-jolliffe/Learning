from datetime import date

def days_diff(date1, date2):
    '''give two tuples in the form (yyyy, m, d) representing start and end
       dates, calculates total days between the two dates'''

    #unpack each tuple into an int and feed into date as arg
    d0 = date(date1[0], date1[1], date1[2])
    d1 = date(date2[0], date2[1], date2[2])

    #calc difference between to dates
    delta = abs(d1 - d0)
    print (delta.days)

days_diff((2009, 1, 1), (2018, 1, 1))
