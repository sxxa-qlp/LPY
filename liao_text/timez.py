import re 
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
	localt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	tz = int(re.match(r'UTC([+-]\d+):\d\d', tz_str).group(1))
	print(tz)
	localt = localt.replace(tzinfo = timezone(timedelta(hours=tz)))
	a = localt.timestamp()
	return a

c = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert c == 1433121030.0,





