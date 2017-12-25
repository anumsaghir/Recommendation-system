from datetime import date

birthdays = {
    date(year=1980, month=12, day=12): ['Picolo', 'Goku'],
    date(year=1950, month=12, day=24): ['Rob Stark', ],
    date(year=1950, month=10, day=11): ['John', ],
    date(year=1980, month=12, day=26): ['Sara', ],
    date(year=1950, month=10, day=10): ['Ali', ],
    date(year=1982, month=12, day=26): ['Herry', ],
    date(year=1950, month=10, day=25): ['Shark', ]    
}
today = date.today()
print(today)
#birthday = list(birthdays.keys())
#print(birthday)
#birthday1 = list(birthdays.values())
#print(birthday1)
#def checkTodaysBirthdays():

found_birthdays = False

for b_date, names in birthdays.items():
    if b_date.month == today.month and b_date.day == today.day:
        found_birthdays = True
        for name in names:
          print("!!! Happy Birthday %s !!!" % name)

if found_birthdays is False:    
    print("Sorry no birthdays today")

#if birthdays.keys().month == date.today().month:
   # if (birthdays.keys().day == date.today().day):
   #     print("Happy Bithday", 'birthdays_value()')
    #else:
     #   print("sorry no birthday today")
#else:
 #   print("No Birthday Today")


