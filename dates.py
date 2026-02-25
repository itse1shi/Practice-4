from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print(five_days_ago)

###########################################

from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)

###########################################

from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print(no_microseconds)

###########################################

from datetime import datetime

date1 = datetime(2026, 2, 25, 12, 0, 0)
date2 = datetime(2026, 2, 24, 6, 30, 0)

delta = date1 - date2
seconds = delta.total_seconds()

print(seconds)