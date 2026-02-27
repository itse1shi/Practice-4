import datetime

def parse(line):
    date_part, time_part, tz_part = line.strip().split()
    dt = datetime.datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    sign = 1 if '+' in tz_part else -1
    h, m = map(int, tz_part[4:].split(':'))
    offset = datetime.timedelta(hours=h, minutes=m)
    return dt - offset if sign == 1 else dt + offset

start = parse(input())
end = parse(input())

print(int((end - start).total_seconds()))