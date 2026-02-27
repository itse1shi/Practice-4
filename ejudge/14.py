import datetime

def parse(line):
    date_part, tz_part = line.strip().split()
    dt = datetime.datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if '+' in tz_part else -1
    hours, minutes = map(int, tz_part[4:].split(':'))
    offset = datetime.timedelta(hours=hours, minutes=minutes)
    return dt - offset if sign == 1 else dt + offset

dt1 = parse(input())
dt2 = parse(input())

diff = abs(dt1 - dt2)
print(diff.days)