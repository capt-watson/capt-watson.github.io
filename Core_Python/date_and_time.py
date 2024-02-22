#! A program to measure the time in seconds since the epoch.

# import time

## epoch time = lapsed in seconds since beginning of current year

# epoch = time.time() ## call time() method of time module

## convert the epoch time into a time_struct object t

# t = time.localtime(epoch)

## retrieve the date from the structure t

# d = t.tm_mday
# m = t.tm_mon
# y = t.tm_year

# print('Current Date is: %d-%d-%d ' %(d,m,y))
#~ Current Date is: 9-2-2024 

# d = t[2]
# m = t[1]
# y = t[0]

# print('Current Date is: %d-%d-%d ' %(d,m,y))
#~ Current Date is: 9-2-2024 

## Retrieve time from the structure t

# h = t[3]
# m = t[4]
# s = t[5]

# print('Current time is: %d-%d-%d ' %(h,m,s))
#~ Current time is: 11-35-52 

## Retrieve day of the week - today, yesterday, DST, Time zone name

# td = t[6]       ## Monday is 0
# yd = t[7]
# dst = t[8]      ## No DST = 0
# tz = t.tm_zone

# print('Today, Yesterday, DST and Time zone is: %d-%d-%d-%s ' %(td,yd,dst,tz))
#~ Today, Yesterday, DST and Time zone is: 4-40-0-India Standard Time

#! A program to convert epoch time into corresponding date & time using
#! 'ctime() function' of 'time' module.

# t = time.ctime(epoch)
# print(t)
#~ Fri Feb  9 11:48:35 2024

#@ Date and Time Now

#! Program to know the current date and time various built in functions
#@ now() method

# from datetime import datetime

# now= datetime.now()        ## returns datetime class object

# print('Date Today: {}-{}-{}'.format(now.day, now.month, now.year))
# #~ Date Today: 9-2-2024

# print('Time Now: {}:{}:{}'.format(now.hour, now.minute, now.second))
# #~ Time Now: 12:23:2

#@ today() method

# from datetime import *

# dtm = datetime.today()
# print('Today\'s date & time = ',dtm)
#~ Today's date & time =  2024-02-09 12:21:50.521805

# td = date.today()
# print('Today\'s Date: ',td)
# #~ Today's Date:  2024-02-09

#@ Combining Date & Time

#! A program to create a datetime object by combining date and time objects

# from datetime import *
# d = date(2024, 2, 9)
# t = time(13,45)
# dt = datetime.combine(d,t)
# print(dt)

#! A program to create a datetime object and change its content

# from datetime import *
# dt1 = datetime(year= 2024, month=2, day=9, hour=13, minute=55, second=00)
# print(dt1)

# ## Change its year, month and hour values
# dt2 = dt1.replace(year=2025, hour=14, month= 3)
# print(dt2)

#@ formatting date & times

#% strftime() method = string format of time method

#! A program to convert a date into a required string format


# from datetime import *

# ## get date into a td object

# td = datetime.now()

# # format td and convert into string str

# str = td.strftime('%d %B %Y')
# print(str)
# #~ 09 February 2024

# str = td.strftime('%a, %d %B %Y')
# print(str)
# #~ Fri, 09 February 2024

# str = td.strftime('%H:%M:%S')
# print('Current Time is: ',str)
# #~ Current Time is:  15:35:04

# str = td.strftime('%I:%M:%S')
# print('Current Time is: ',str)
# #~ Current Time is:  03:35:59

# str = td.strftime('%I:%M:%S %p')
# print('Current Time is: ',str)

# #~ Current Time is:  03:36:50 PM

#! A program to find the day of the year and week day name.

# from datetime import *

## get today's date

# td = date.today()
# # print(td)

# s1 = td.strftime('%j')  ## returns days of the year from 1st January.
# print('Today is the', s1+'th day of the year')

# s2 = td.strftime('%A')
# print('Today is: ',s2)

#! To enter date from the keyboard and display it as day of the week:

# d,m,y = [int(x) for x in input('Enter a date: ').split('/')]

# dt = date(y,m,d)

# print(dt.strftime('Day %w of the week. This is %A'))

#! Find the difference in number of days, weeks and months between two given
#! dates

# from datetime import *

# ## Enter two dates from the keyboard

# d1,m1,y1 = [int(x) for x in input('Enter First Date: ').split('/')]
# d2,m2,y2 = [int(x) for x in input('Enter Second date: ').split('/')]

# ## create date class objects with the input

# dt1 = date(y1,m1,d1)        ## Always write in yyyy,mm,dd format
# dt2 = date(y2,m2,d2)        ## Always write in yyyy,mm,dd format


# ## find the difference between these two dates

# dt = dt1-dt2
# print('Difference between these two dates= ',dt)

# ## Find difference in weeks

# weeks, days = divmod(dt.days, 7)
# print('Weeks difference = ',weeks)

# ## find difference in months

# months, days= divmod(dt.days, 30)
# print('Months Difference: ',months)

#~ Difference between these two dates=  1715 days, 0:00:00
#~ Weeks difference =  245
#~ Months Difference:  57

#@ Find difference between two dates along with times

# from datetime import *

# d1 = datetime(2024, 2, 9, 17, 00, 50)
# d2 = datetime(2019, 5,31,14,00,15)

# diff = d1-d2
# print(diff)

# ## Divide days by 7 to get weeks and remaining days

# weeks, days = divmod(diff.days, 7)

# ## Divide seconds by 3600 to get hours and remaining seconds

# hrs, secs = divmod(diff.seconds, 3600)

# ## Divide remaining seconds to by 60 to get minutes

# mins = secs//60

# ## Take remaining seconds from the remainder of the division
# secs = secs%60

# print('Difference is: %d weeks, %d days, %d hours, %d minutes and %d seconds' %(weeks, days, hrs, mins, secs))

#@ Finding Duration using 'timedelta'

#! Find out the future date and time from an existing date and time

# from datetime import *

# ## store date and time in a datetime object

# d1 = datetime(2024,2,10,9,40,00)

# ## define the duration using timedelta object

# period1 = timedelta(days=3650, seconds= 10, minutes=20, hours=12)

# ## add the duration to d1 and display
# print('The new date and time is: ',d1+period1)

#! Display the next 10 days continuously

# from datetime import *

# ## start with today

# d = date.today()
# #print(d)


# ## or any other date
# d = date(1980, 4, 29)

# ## add 1 to 9 days and get future dates

# for x in range(1,10):
#     next_date = d+timedelta(days=x)
#     print(next_date)
    
#@ Comparing Two dates

#! Accept date of births of two persons and determine the older person

# from datetime import *

# ## enter the birth dates and store them into date object class

# d1,m1,y1 = [int(x) for x in input('Enter 1st Person\'s date of birth: ').split('/')]

# b1 = date(y1,m1,d1)

# d2,m2,y2 = [int(x) for x in input('Enter 2nd person\'s date of birth: ').split('/')]

# b2 = date(y2,m2,d1)

# ## compare the birth dates

# if b1 == b2:
#     print('Both person are of the same age')
# elif b1 > b2:
#     print('The second person is older') ## Due younger person having higher dob
# else:
#     print('The first person is older')

#@ Sorting dates

## Best ways to sort a group of dates is to store them into and then apply list's
## sort method

#! Sort a group of given dates in a ascending order

# from datetime import *

# ## take an empty list

# group = []

# ## Add today's date to the list

# group.append(date.today())

# ## create some more dates and append them to the list

# d = date(1959,6,18)
# group.append(d)

# d = date(1964,7,1)
# group.append(d)

# ## Add 25 days to the date and add to list

# group.append(d+timedelta(days=25))

# ## sort the list

# group.sort()

# for x in group:
#     print(x)
 
#@ Stopping execution Temporarily

#% To stop execution of a program temporarily for a given amount of time, sleep()
#% method of time module is used.

#! Generate random numbers in a range with some time delay between each number

# import time, random

# ## generate 10 random numbers

# for i in range(10):
#     ## generate in range of 100 to 200
#     num = random.randrange(100, 200, 5)
#     print(num)
    
#     ## suspend execution for 3.5 seconds
#     time.sleep(3.5)

#@ Knowing the time taken by a program

#% perf_counter()
#! This function returns the time taken in fractional seconds to measure the time
#! taken by the program to execute a group of statements. It also includes the time
#! elapsed during sleep of the processor.

#% process_time()
#! Returns the time duration in fractional seconds to measure the total time taken
#! by the program and CPU in executing a group of statements. BUT WILL NOT COUNT
#! THE TIME ELAPSED DURING THE SLEEP OF THE PROCESSOR.

#& The performance of a program is obtained through perf_counter() function

#! Find the execution time of a program.

# from time import *

# # ## Will note the starting time of the program
# # t1 = perf_counter()

# # ## do some processing

# # i, sum = 0,0
# # while i < 1000000:
# #     sum += 1
# #     i += 1

# # ## make the processor or PVM sleep for 3 seconds
# # ## This is also measured by the perf_counter()

# # sleep(3)

# # ## Will note the ending time of the program

# # t2 = perf_counter()

# # ## Total execution time in seconds)
# # print('Total Execution Time: %f seconds' % (t2-t1))

# # #~ Total Execution Time: 3.116918 seconds


# from time import *

# ## Will note the starting time of the program
# t1 = process_time()

# ## do some processing

# i, sum = 0,0
# while i < 1000000:
#     sum += 1
#     i += 1

# ## make the processor or PVM sleep for 3 seconds
# ## This is also measured by the perf_counter()

# sleep(3)

# ## Will note the ending time of the program

# t2 = process_time()

# ## Total execution time in seconds)
# print('Total Execution Time: %f seconds' % (t2-t1))

# #~ Total Execution Time: 0.078125 seconds


#@ Working with calendar Module

## To test whether leap year or not

from calendar import *

y = int(input('Enter year: '))

if isleap(y):
    print(y, 'is a leap year.')
else:
    print(y, 'is not a leap year.')

# #~  1959 is not a leap year.
# #~  2024 is a leap year.


#! Display calendar of given month of the year

# from calendar import *

# yy = int(input('Enter year: '))
# mm = int(input('Enter month: '))

# ## Display the calendar of the requested month

# str = month(yy,mm)

# print(str)

#! Display the calendar for all the month of a given year

#% calendar(year, w=2, l=1, c=6, m=3)  default values given here.

#* 'w' represents the width between two columns
#* 'l' represents the blank lines between two rows
#* 'c' represents column wise space between two months
#* 'm' represents number of months to be displayed in a row

#% note: Values of 'w', 'l', 'c' and 'm' are not compulsory

# from calendar import *

# year = int(input('Enter year: '))
