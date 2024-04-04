from datetime import datetime, date, timedelta


dt1 = datetime.now()
# print(dt1.strftime('%d-%b-%Y  %I:%M:%S:%p'))

# print(dt1.strftime('%Y'))
# print(dt1.strftime('%b'))
# print(dt1.strftime('%d'))
# print(dt1.strftime('%I'))
# print(dt1.strftime('%M'))
# print(dt1.strftime('%S'))
# print(dt1.strftime('%f'))
# print(dt1.strftime('%Z'))

# dt2 =datetime(day=29, month=2, year=2024)
# print(dt2.strftime('%d %b %Y %H:%M:%S'))

# dt3 =dt1.date()
# print(dt3.strftime('%d %b %Y'))

# dt2 = dt1.time()
# print(dt2)

## Add 5 days to today's date
dt4 = date.today() + timedelta(days=5)
# print(dt4.strftime('%d-%m-%Y'))

## Subtract 5 days from today's date
dt5 = date.today() - timedelta(days=5)
# print(dt5.strftime('%d-%m-%Y'))

if dt4 > dt5:
    print(dt4.strftime('%d-%m-%Y'),'is greater than', dt5.strftime('%d-%m-%Y'))
elif dt5 < dt4:
    print(dt5.strftime('%d-%m-%Y'),'is less than', dt4.strftime('%d-%m-%Y'))
else:
    print(dt4.strftime('%d-%m-%Y'), 'is equal to', dt5.strftime('%d-%m-%Y'))

## Add 5 minutes to current time

ct = datetime.now()+timedelta(minutes=5)
print('5 minutes later the time will be: ',ct.strftime('%I:%M:%S'))
