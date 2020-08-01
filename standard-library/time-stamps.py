import time
from datetime import datetime, timedelta

#  Time
def send_emails():
    for i in range(10000000):
        pass

start = time.time()
send_emails()
end = time.time()
print(end - start)

#  Date Time
dt = datetime(2018, 1, 1) + timedelta(days=1)
print(datetime.now())
print(datetime.strptime("2018/01/01", "%Y/%m/%d"))

newTime = time.time()
newDateTime = datetime.fromtimestamp(newTime)
print(newDateTime)

print(f"{dt.year}/{dt.month}")
print(newDateTime.strftime("%Y/%m"))

#  Time Deltas
duration = newDateTime - dt
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())
