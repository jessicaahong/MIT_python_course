"""Wed May 11 2016"""
import unittest

def zellers_alg(A, B, C, D):
	'''
	where A, B, C, D are all integers >= 1.
	A = the month of the year, with March having the value 1, April the
	value 2, . . ., December the value 10, and January and February being
	counted as months 11 and 12 of the preceding year (in which
	case,subtract 1 from C)
	B = the day of the month (1, 2, 3, . . . , 30, 31)
	C = the year of the century (e.g. C = 89 for the year 1989)
	D = the century (e.g. D = 19 for the year 1989)
	'''
	error = "Invalid input"
	# If any of the inputs are not integers, or if the month/day/year/century values are invalid, return error
	if (type(A) != int or type(B) != int or type(C) != int or type(D) != int or\
		A <= 0 or B <= 0 or C < 0 or D < 0):
		return error
	if (A > 12):
		return error
	if (B > 31):
		return error
	# If A == 11 or 12, treat them as months 11 and 12 belonging to the preceding year (subtract 1 from C)
	if A > 10:
		C -= 1
	# Realized that we need to accommodate for edge cases such as turn of the century
	# If the year was 1900 and it's January or February, algorithm must be tweaked to roll back 1 century (D -= 1) and set year to 99 (C = 99)
	if C == -1:
		D -= 1
		C = 99

	W = (13*A - 1) / 5
	X = C / 4
	Y = D / 4
	Z = W + X + Y + B + C - 2 * D
	R = Z % 7
	if R < 0:
		return (R + 7)
	else:
		return R

def zellers_statement():
	f_name = raw_input("Enter your first name: ")
	l_name = raw_input("Enter your last name: ")
	mo_str = raw_input("What month were you born in?\n\
	Please enter a number between 1 and 12 where March is 1 and February is 12: ")
	day_str = raw_input("What day of the month were you born on?\n\
	Please enter a number between 1 and 31: ")
	year_str = raw_input("What year were you born in?\n\
	Please enter complete year (e.g. 1950): ")

	# Check to make sure month, day, year are integers
	try:
		mo = int(mo_str)
		day = int(day_str)
		year = int(year_str)
		print "THIS IS THE YEAR %s" % year
	# If any one is not, print error message and display prompts again (make recursive call)
	except ValueError:
		print "Birthdate input is invalid."
		zellers_statement()
	else:
		# Calculate year of century using modulus operator, century using division
		yr_century = year % 100
		century = year / 100
		# Plug transformed variables into zellers_alg function, save return value to variable result
		result = zellers_alg(mo, day, yr_century, century)
		# Create variable day_of_week based on result. If result is not an integer between 1-6, return error from zellers_alg function
		if result == 0:
			day_of_week = "Sunday"
		elif result == 1:
			day_of_week = "Monday"
		elif result == 2:
			day_of_week = "Tuesday"
		elif result == 3:
			day_of_week = "Wednesday"
		elif result == 4:
			day_of_week = "Thursday"
		elif result == 5:
			day_of_week = "Friday"
		elif result == 6:
			day_of_week = "Saturday"
		else:
			print result
			return
		message = "%s %s was born on a %s." % (f_name, l_name, day_of_week)
		print message
		return message

zellers_statement()

class TestZellersAlg(unittest.TestCase):
	def testAlg(self):
		self.assertEqual(zellers_alg(6,17,91,19), 6)
		self.assertEqual(zellers_alg(11,1,00,18), 3)
		self.assertEqual(zellers_alg(11,15,00,22), 3)
		self.assertEqual(zellers_alg(4,-17,61,18), "Invalid input")
		self.assertEqual(zellers_alg(1,1,"banana", "banana"), "Invalid input")

if __name__ == '__main__':
	unittest.main()