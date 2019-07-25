#Python is for everybody!
#Chapter 6: Strings
#Exercise 5: Take the following Python code that stores a string: 
#str='X-DSPAM-Confidence:0.8475
#Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
end = len(str)

#stores the string after the colon in the variable str into the variable number 
number = str[start+1:end]

#store the string from the variable number as a floating point number in the variable fpnumber 
fpnumber = float(number)


#print number
#print fpnumber