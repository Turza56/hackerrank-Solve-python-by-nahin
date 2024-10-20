
from datetime import datetime
date = list(map(int, input().split()))
date_time = datetime(date[-1],date[0],date[-2])
find_day = date_time.strftime("%A")

print(find_day.upper())
