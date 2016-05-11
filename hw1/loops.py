"""Tue May 10 2016"""

print "********** Exercise 2.2 Part 1 **********"

def to_decimals():
	for num in range(2,11):
		print 1/float(num)

print "********** Exercise 2.2 Part 2 **********"

def countdown():
	start = raw_input("Choose a number to count down to zero from! ")
	# Check that user input is an integer
	try:
		start_integer = int(start)
	except ValueError:
		print "In order to countdown to zero, input must be a positive integer!"
	else:
	# Check that user input is a positive integer
		if start_integer > 0:
			while start_integer >= 0:
				print start_integer
				start_integer -= 1
		else:
			print "In order to countdown to zero, input must be a positive integer!"

print "********** Exercise 2.2 Part 3 **********"

def calculate_exponential():
	# Have the answer if inputs are exponents, must accomodate for if they are floats
	base = raw_input("Choose a base! ")
	exponent = raw_input("Choose an exponent! ")
	# try:
	# 	 base = float(raw_input("Choose a base! "))
	# 	 exponent = float(raw_input("Choose an exponent! "))
	# except ValueError:
	# 	print "Input is invalid. You must pick two numbers."
	# 	return
	if (type(base) != int) or (type(exponent) != int):
		print "Input is invalid. You must pick two numbers."
		return
	solution = base
	for num in range(1, exponent):
		solution *= base
	print solution

print "********** Exercise 2.2 Part 4 **********"

def divisible_by_2():
	number = raw_input("Enter a number that is divisible by two. ")
	# Check that input is an integer
	try:
		integer = int(number)
	except ValueError:
		print "Nope. Try again."
		divisible_by_2()
	# If input is an integer, check that it is divisible by two with no remainder
	else:
		if integer % 2 == 0:
			print "Huzzah!"
		else:
			print "Nope. Try again."
			divisible_by_2()


