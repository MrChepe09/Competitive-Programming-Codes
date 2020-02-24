from datetime import date
def numofdays(date1, date2):
  return (date2-date1).days

a = list(map(int, input().split('-')))
date1= date(a[0], a[1], a[2])
b = list(map(int, input().split('-')))
date2= date(b[0], b[1], b[2])
print(abs(numofdays(date1, date2)))
