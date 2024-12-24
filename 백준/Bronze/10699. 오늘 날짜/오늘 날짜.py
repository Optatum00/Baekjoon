import datetime as dt
x = dt.datetime.now()
y = x.year
m = x.month
d = x.day
h = x.hour
min = x.minute

if h > 3 or (h == 3 and min == 0):
    d = d+1

if m < 10:
    m = '0'+str(m)

if d < 10:
    d = '0'+str(d)

print(f'{y}-{m}-{d}')