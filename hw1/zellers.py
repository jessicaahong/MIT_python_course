"""Wed May 11 2016"""

def zellers_alg(A, B, C, D):
	error = "Invalid input"
	if (type(A) != int or type(B) != int or type(C) != int or type(D) != int or\
		A <= 0 or B <= 0 or C < 0 or D < 0):
		return error
	if (A > 12):
		return error
	if (B > 31):
		return error
	if A == 11 or A == 12:
		C -= 1
	# Realized that we need to accommodate for edge cases such as turn of the century
	# If the year was 1900 and it's January or February, algorithm must be tweaked to roll back 1 century and set year to 99
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

	try:
		mo = int(mo_str)
		day = int(day_str)
		year = int(year_str)
		print "THIS IS THE YEAR %s" % year
	except ValueError:
		print "Birthdate input is invalid."
		zellers_statement()
	else:
		# Tried to accommodate for years prior to year 1000
		if len(year_str) <= 2:
			century = 0
			yr_century = int(year_str)
		elif len(year_str) == 3:
			century = int(year_str[0])
			print "THIS IS THE CENTURY %s" % century
			yr_century = int(year_str[1:3])
			print "THIS IS THE YR_CENTURY %s" % yr_century
		else:
			century = int(year_str[0:(len(year_str)-2)])
			yr_century = int(year_str[(len(year_str)-2):len(year_str)])
		result = zellers_alg(mo, day, yr_century, century)
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
			return result
		message = "%s %s was born on a %s." % (f_name, l_name, day_of_week)
		print message
		return message

import unittest

class TestZellersAlg(unittest.TestCase):
	def testAlg(self):
		self.assertEqual(zellers_alg(6,17,91,19), 6)
		self.assertEqual(zellers_alg(11,1,00,18), 3)
		self.assertEqual(zellers_alg(4,-17,61,18), "Invalid input")
		self.assertEqual(zellers_alg(1,1,"banana", "banana"), "Invalid input")

if __name__ == '__main__':
	unittest.main()