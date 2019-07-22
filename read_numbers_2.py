#Python is for Everybody!
#5.9 Exercises
#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maxinumum and minimum of the numbers instead of the average.

count = 0
total = 0
largest = None
smallest = None
while True:
	number = input('Enter a number: ')
	if number == 'done': break
	number = float(number)
	
	# Set the first number entered as both the largest and smallest value
	if largest is None and smallest is None:
		largest = number
		smallest = number
		
	# If number entered is > the previous largest number entered, set the
	# current number as the largest number.
	elif number > largest:
		largest = number
		
	# If number entered is < the previous smallest number entered, set the
	# current number as the smallest number.
	elif number < smallest:
		smallest = number 
	count = count + 1 
	total = total + number
	print(number)
	
print('Total: ', total)
print('Count: ', count)
print('Average: ', total/count)
print('Largest: ', largest)
print('Smallest: ', smallest)
