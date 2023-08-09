import datetime
from datetime import time   # importing time separateley



date_object = datetime.date(2023,5,8) # creates an date object
print(date_object)
print(type(date_object))

present_date = datetime.date.today()   # creates present date object
print(present_date)

print(present_date.year)
print(present_date.month)
print(present_date.day)




time_object = time(11,36,33)
print(time_object)
print(time_object.hour)
print(time_object.minute)
print(time_object.second)
print(time_object.max)
print(time_object.min)
