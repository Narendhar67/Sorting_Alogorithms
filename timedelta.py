from datetime import timedelta, datetime

date = datetime.now()
print(date)

delta = timedelta(days=32 , hours = 13)   # timdelta is a period of time

new_date = date + delta
print(new_date)
print(date-delta)

print(new_date - date) # time difference between dates , i.e timedelta