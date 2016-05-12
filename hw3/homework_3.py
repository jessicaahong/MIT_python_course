"""Thurs May 12 2016"""

##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 ********** 

# Bugs
'''Aside '''
##### BUG 1 #####
'''The large_num function sets variable res to a boolean, but never actually returns a value'''

# def large_num(num):
#     res = (num > 10000)
#     return res


##### BUG 2 #####
'''
The 3 lines that constitute the test written for negate(b) are very confusing. 
The first line of the test calls the function using b as an argument, but doesn't provide any context for the returned value.
The second line sets a variable equal to num (which has not been defined).
Running this test should provide context that clearly defines both the argument value and the returned value.
'''

# print num = 3
# print 'num =', num, ' negate(num):', negate(num)

# # OR

# print 'num = 3, negate(num):', negate(3)

##### BUG 3 #####
'''
The two lines that test function large_num don't explicitly declare the value of the argument they're using.
The test should clearly define both the argument being passed to large_num, and the returned result.
You should also test to see what happens when you pass a number > 10000 to the function, and what happens when you pass a number < 10000 to the function.
'''

# print "1000 is not greater than 10000, large_num(1000) returns", large_num(1000)
# print "15000 is greater than 10000, large_num(15000) returns", large_num(15000)

# **********  Exercise 5.2 ********** 

# Define "Mutable" and list what data structures have this characteristic

# lists


# Define "Immutable" and list what data structures have this characteristic


# strings
# tuples

# **********  Exercise 5.3 **********

import math

def ball_collide(ball1, ball2):
    '''
    Computes whether or not two balls are colliding

    ball1: a tuple of (x-coord, y-coord, radius) nums (ints or floats);
    represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints or floats); 
    represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    # calculate the sum of the two radii
    radii_sum = ball1[2] + ball2[2]
    # calculate the distance between the two ball centers
    distance = math.sqrt(((ball1[0] - ball2[0])**2) + ((ball1[1] - ball2[1])**2)) 
    # if the distance between the two balls is <= the sum of the two radii, the balls are colliding; return True
    if distance <= radii_sum:
        return True
    # if the distance between the two balls is > the sum of the two radii, the balls are not colliding; return False
    else:
        return False
    

# Test Cases for Exercise 5.3
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True


# **********  Exercise 5.4 **********

class_dict = {"IB117": "Medical Ethnobotany", "IB127L": "Motor Control with Laboratory", "IB152": "Environmental Toxicology", "PACS164A": "Introdution to Nonviolence"}


def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    ##### YOUR CODE HERE #####
    
    

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    ##### YOUR CODE HERE #####

    

# Test Cases for Exercise 5.4
##### YOUR CODE HERE #####



# **********  Exercise 5.5 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys and values generated
      from the file, as specified in Exercise 5.5.
    '''
    ## Your Code Here ##
    


def changeEntry(addrBook, entry, field, newValue):
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    ## Your Code Here ##
