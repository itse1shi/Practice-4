import datetime

def parse(line):
    date_part, tz_part = line.strip().split()
    dt = datetime.datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if '+' in tz_part else -1
    h, m = map(int, tz_part[4:].split(':'))
    offset = datetime.timedelta(hours=h, minutes=m)
    return dt - offset if sign == 1 else dt + offset

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

birth_line = input().strip()
current_line = input().strip()

birth_date, birth_tz = birth_line.split()
bm = int(birth_date[5:7])
bd = int(birth_date[8:10])

sign = 1 if '+' in birth_tz else -1
h, m = map(int, birth_tz[4:].split(':'))
birth_offset = datetime.timedelta(hours=h, minutes=m)

current_utc = parse(current_line)

def birthday_utc(year):
    d = bd
    if bm == 2 and bd == 29 and not is_leap(year):
        d = 28
    local = datetime.datetime(year, bm, d)
    return local - birth_offset if sign == 1 else local + birth_offset

cand = birthday_utc(current_utc.year)
if cand < current_utc:
    cand = birthday_utc(current_utc.year + 1)

diff_seconds = (cand - current_utc).total_seconds()
print(int((diff_seconds + 86399) // 86400))