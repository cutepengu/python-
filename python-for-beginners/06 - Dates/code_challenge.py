# print today's date
from datetime import datetime, timedelta
current_date = datetime.now()
print(current_date)
# print yesterday's date
one_day = timedelta(days=1)
yesterday = today - one_day
print('yesterday was: ' + str(yesterday))
# ask a user to enter a date
enter_date = input('enter a date: (dd/mm/yyyy) ')
enter_date = datetime.strptime(enter_date, '%d/%m/%Y')
# print the date one week from the date entered
one_week = timedelta(weeks=1)
last_week = today + one_week
print('next week is: ' + str(last_week))