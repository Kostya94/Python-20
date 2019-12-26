import datetime
new = datetime.datetime.now()
then = datetime.datetime(2019, 12, 12)
rez = new - then
print(rez.days)