import time
import datetime
'''
Time in seconds since the epoch: 1528783285.288818
Current date and time:  2018-06-12 11:31:25.289190
Or like this:  18-06-12-11-31
Or like this:  18-06-12-11-35-2018
Current year:  2018
Month of year:  June
Week number of the year:  24
Weekday of the week:  2
Day of year:  163
Day of the month :  12
Day of week:  Tuesday
Saturday

'''
''' write g(0)
'''

print( "Time in seconds since the epoch: %s" %time.time())
# Time in seconds since the epoch: 1528783285.288818
print( "Current date and time: " , datetime.datetime.now())
# Current date and time:  2018-06-12 11:31:25.289190

print( "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
# Or like this:  18-06-12-11-31

print( "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%Y "))
# Or like this:  18-06-12-11-35-2018

print( "Current year: ", datetime.date.today().strftime("%Y"))
# Current year:  2018

print( "Month of year: ", datetime.date.today().strftime("%B"))
# Month of year:  June

print( "Week number of the year: ", datetime.date.today().strftime("%W"))
# Week number of the year:  24

print( "Weekday of the week: ", datetime.date.today().strftime("%w"))
# Weekday of the week:  2

print( "Day of year: ", datetime.date.today().strftime("%j"))
# Day of year:  163

print( "Day of the month : ", datetime.date.today().strftime("%d"))
# Day of the month :  12

print( "Day of week: ", datetime.date.today().strftime("%A"))
# Day of week:  Tuesday

mydate = datetime.date(1943,3, 13)  #year, month, day
print(mydate.strftime("%A"))
# Saturday
filename =  datetime.date.today().strftime("%d-%B") + '-' + datetime.datetime.now().strftime("%H-%M") + '-PM' + '.txt'
f = open(filename,'w')
f.write('Tejas is a bad boy')
f.close()
