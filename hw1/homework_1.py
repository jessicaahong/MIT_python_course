"""Tue May 10 2016"""

##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

print "  |  |  \n--------\n  |  |  \n--------\n  |  |  "

# Alternatively...

# print "  |  |  "
# print "--------"
# print "  |  |  "
# print "--------"
# print "  |  |  "

print "********** Exercise 1.3 **********"

cells = "  |  |  "
line = "--------"
new = "\n"

# Applying usage of variables to 1.2 answer, but ends up being more typing

print cells + new + line + new + cells + new + line + new + cells

# Alternatively...

# print cells
# print line
# print cells
# print line
# print cells

print "********** Exercise 1.4 **********"

f_name = raw_input("Enter your first name: ")
l_name = raw_input("Enter your last name: ")
mo = raw_input("Enter your date of birth:\nMonth? ")
day = raw_input("Day? ")
year = raw_input("Year? ")
print "%s %s was born on %s %s, %s." % (f_name, l_name, mo, day, year)

