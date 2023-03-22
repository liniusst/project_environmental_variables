# Write a function that returns dates of the 5 upcoming Friday 13ths, with Year, month and date
import datetime
# from datetime import datetime

# today = datetime.w
# print(today.date)

# x = today.weekday()
# print('day Name:', today.strftime('%A'))
# print(x)


from_years = datetime.date.today().year
from_month = datetime.datetime.today().month
dates_found = 0

for y in range(from_years, 2199):
    for m in range(from_month, 13):
        if datetime.date(y, m, 13).weekday() == 4 and dates_found <= 4:
            print(datetime.date(y, m, 13))
            dates_found += 1



