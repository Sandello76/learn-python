"""
1 Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2 Превратите строку "01/01/25 12:10:03.234567" в объект datetime
"""
import locale
from datetime import datetime, date, timedelta
locale.setlocale(locale.LC_TIME, 'russian')
dt_now = datetime.now()

delta1 = timedelta(days=1)
delta2 = timedelta(days=30)

dt_str = "01/01/25 12:10:03.234567"
dt_str_convert = datetime.strptime(dt_str, '%d/%m/%y %H:%M:%S.%f')

today = dt_now
yestoday = dt_now - delta1
month = dt_now - delta2

print(yestoday.strftime('%A %d %B %Y'))
print(today.strftime('%A %d %B %Y'))
print(month.strftime('%A %d %B %Y'))
print("Дата и время:", dt_str_convert)