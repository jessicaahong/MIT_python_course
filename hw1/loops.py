"""Tue May 10 2016"""

print "********** Exercise 2.2 Part 1 **********"

def to_decimals():
	for num in range(2,11):
		print 1/float(num)

print "********** Exercise 2.2 Part 2 **********"

def countdown():
	start = raw_input("Let's count down to zero! Choose a positive integer: ")
	# Check that user input is an integer. If not, print error message.
	try:
		start_integer = int(start)
	except ValueError:
		print "In order to countdown to zero, input must be a positive integer!"
	else:
		# Check that user input is a positive integer.
		if start_integer > 0:
			while start_integer >= 0:
				print start_integer
				start_integer -= 1
		# If user input is not a positive integer, print error message.
		else:
			print "In order to countdown to zero, input must be a positive integer!"

print "********** Exercise 2.2 Part 3 **********"

def calculate_exponential():
	# Ask for user input
	base = input("Choose a base! ")
	exponent = input("Choose an exponent! ")
	# If user input is not an integer, print error message and return
	if (type(base) != int) or (type(exponent) != int):
		print "Input is invalid. You must pick two integers."
		return
	# Create solution variable, set equal to base
	solution = base
	# If exponent is 0 or we're calculating 0**0, our loop won't work. Print 1 instead.
	if exponent == 0 or (exponent == 0 and base == 0):
		print 1
	else:
		# For loop to calculate solution, use absolute value of exponent to accommodate negative exponent inputs
		for num in range(1, abs(exponent)):
			solution *= base
		# Return solution (solution variable transformed to reciprocal decimal value if exponent was negative)
		if exponent > 0:
			print solution
		elif exponent < 0:
			print 1/float(solution)

print "********** Exercise 2.2 Part 4 **********"

def divisible_by_2():
	number = raw_input("Enter a number that is divisible by two: ")
	# Check that number is an integer. If not, print error message and make recursive call.
	try:
		integer = int(number)
	except ValueError:
		print "Nope. Try again."
		divisible_by_2()
	# If number is an integer, check that it is divisible by two with no remainder.
	else:
		if integer % 2 == 0:
			print "Huzzah!"
		# If number is not divisible by two, print error message and make recursive call.
		else:
			print "Nope. Try again."
			divisible_by_2()


calculate_exponential()