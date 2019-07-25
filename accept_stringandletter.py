#Python is for Everybody!
#Chapter 6: Strings
#Exercise 3: Encapsulate this code in a function named cont, and generalize it so that it accepts the string and the letter as arguments.
def count(str, ch):
	banana = str
	count = 0
	for char in banana:
		if char == ch:
			count = count + 1
	print (count)