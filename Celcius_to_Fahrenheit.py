inp=input("Enter Fahrenheit Temperature:")
try:
	fahr=float(inp)
	cel=(fahr-32.0)*5.0/9.0
	print(cel)
except:
	print("please enter a number")