import datetime
import pytz

today = datetime.date.today()
# print(today)

brithday = datetime.date(2001, 2, 10)
# print(brithday)
# print(repr(brithday))

days_since_brith = today - brithday
# print(days_since_brith)

days_since_brith = (today - brithday).days
# print(days_since_brith)

tdelta = datetime.timedelta(days=10)
# print(today + tdelta)
# print(today - tdelta)

# print(today.day)
# print(today.month)
# sunday = 0
# monday = 10
# print(today.weekday())

# print(datetime.time(7, 5, 6, 50))
# datetime.date(y, m, d)
# datetime.time(h, minites, second, mircosecond)
# datetime.datetime( years , month, days , hourse , minites , second , mircosecond)

hourse_delta = datetime.timedelta(hours=10)
# print(datetime.datetime.now())
# print("Add 10 hours ")
# print(hourse_delta + datetime.datetime.now())

datetime_today = datetime.datetime.now(tz=pytz.UTC)
# print(datetime_today)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/pacific'))
# print(datetime_pacific)

# for tz in pytz.all_timezones:
#    print(tz)

""" 
    sting formating with date 
    2019-03-14 -> March 14, 2019
    using strftime (f = formating )
"""
print(datetime_pacific.strftime('%B %d, %y'))

"""
    sting fromating with date
    March 14, 2019 -> datetime(2019,3,14)
    using strping (p = parsing )
"""

# first argument format given after comma
print(datetime_pacific.strptime('March 14, 2019', '%B %d, %Y'))
