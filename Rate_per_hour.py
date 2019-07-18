try:
	hours=input("Please enter number of hours worked here: ")
	hours=int(hours)
except:
	print ("Error, please enter numeric input: ")
	hours=input("Please enter number of hours worked here: ")

overtime_hours=hours-40
print ("You have", overtime_hours, "overtime hours")

#need rate
try:
	rate=input("please enter rate: ")
	rate=int(rate)
except:
	print ("Error, please enter numeric input")
	rate=input("Please enter rate here: ")
	rate=int(hours)

#pay
pay=rate*hours

if overtime_hours>0:
	new_rate=1.5*rate
	overtime_pay=new_rate*overtime_hours
	newPay=hours-overtime_hours
	pay=overtime_pay+newPay*rate
	print ("Your pay is: ", pay)
elif overtime_hours <0:
	pay=rate*hours
	print ("Your pay is: ", pay)