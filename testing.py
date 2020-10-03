from datetime import date, datetime

to = input("Enter Today Date (d/m/y) ")

checkOut = datetime.strptime(to,'%d/%m/%y')

chout = input("Enter Check In Date (d/m/y) ")

checkIn = datetime.strptime(chout,'%d/%m/%y')

print("Today Month ", checkOut.month)
print("Chout Month: ", checkIn.month)

if (checkIn.month == checkOut.month):
    total = (checkOut.day - checkIn.day)
    print(total)
elif (checkIn.month != checkOut.month):
    #days = datetime.date(checkOut) - datetime.date(checkIn)
    dayout = datetime.date(checkOut)
    dayin = datetime.date(checkIn)
    total2 = dayout - dayin
    print(total2)
else:
    print("sucks")
