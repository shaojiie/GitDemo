from datetime import date,timedelta

start = date(2019,1,1)
d2 = date(start.year+1,1,1)
d3 = start+timedelta(days=100)
print(start)
print(d2)
print(d3)