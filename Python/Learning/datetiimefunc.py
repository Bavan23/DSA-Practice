import datetime

today=datetime.date.today()
print(today)


time=datetime.datetime.now()
day=time.strftime("%A")
print(day)
month=time.strftime("%B")
print(month)
time=time.strftime("%H:%M:%S")
print(time)

assigndate=datetime.date(2022,3,2)
print(assigndate)
assigndateandtime=datetime.datetime(2025,1,23,2,3,4)
print(assigndateandtime)