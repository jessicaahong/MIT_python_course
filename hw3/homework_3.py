"""Thurs May 12 2016"""
import csv

##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 ********** 

# Bugs
##### BUG 1 #####
'''The large_num function sets variable res to a boolean, but never actually returns a value

def large_num(num):
    res = (num > 10000)
    return res
'''

##### BUG 2 #####
'''
The 3 lines that constitute the test written for negate(b) are very confusing. 
The first line of the test calls the function using b as an argument, but doesn't provide any context for the returned value.
The second line sets a variable equal to num (which has not been defined).
Running this test should provide context that clearly defines both the argument value and the returned value.


print 'num = 3, negate(num):', negate(3)

'''

##### BUG 3 #####
'''
The two lines that test function large_num don't explicitly print the value of the argument the test is passing.
The test should clearly define both the argument being passed to large_num, and the returned result.


print "large_num(1000) is big?", large_num(1000)
print "large_num(15000) is big?", large_num(15000)
'''

# **********  Exercise 5.2 ********** 

# Define "Mutable" and list what data structures have this characteristic
'''
Mutable objects can be changed in place

Mutable data structures: list, dictionary, set, byte array
'''


# Define "Immutable" and list what data structures have this characteristic
'''
Immutable objects cannot be altered once created

Immutable data structures: integer, float, long, complex, string, tuple, frozen set, bytes
'''


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
print ball_collide((0, 0, 1), (3, 3, 1)), "should be False"
print ball_collide((5, 5, 2), (2, 8, 3)), "should be True"
print ball_collide((7, 8, 2), (4, 4, 3)), "should be True"


# **********  Exercise 5.4 **********

DICTIONARY = {"IB117": "Medical Ethnobotany", "IB127L": "Motor Control with Laboratory", "IB152": "Environmental Toxicology", "PACS164A": "Introdution to Nonviolence"}


def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    class_dict[class_num] = desc
    

def print_classes(dept, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    # MIT class numbers are preceded by a course number, while UC Berkeley class numbers were preceded by department acronym.
    # Adapted print_classes to print out classes I've taken in a given department.

    # Create variable class_numbers, a list of class numbers (keys) contained in the dictionary
    class_numbers = class_dict.keys()
    # Create variable number, a count of how many entries in the dictionary are in the selected department
    number = 0
    for item in class_numbers:
        # If a class has a class number associated with the department, print the class number and name. Increment number by 1.
        if item[0:len(dept)] == dept:
            print "%s - %s" % (item, class_dict[item])
            number += 1
    # If no class numbers are associated with the department, print message
    if number == 0:
        print "No classes taken in that department"
    

# Test Cases for Exercise 5.4
add_class("MCB32","Intro to Human Physiology", DICTIONARY)
print "add_class('MCB32','Intro to Human Physiology', DICTIONARY). Added class MCB32: Intro to Human Physiology to DICTIONARY:",  DICTIONARY
print "Here is the class (1) you've taken in the PACS department. print_classes('PACS', DICTIONARY):", print_classes("PACS", DICTIONARY)
print "You haven't taken any classes in the ENG department. print_classes('ENG', DICTIONARY):", print_classes("ENG", DICTIONARY)



# **********  Exercise 5.5 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys and values generated
      from the file, as specified in Exercise 5.5.
    '''
    # create an empty dictionary that we will fill
    addressBook = {}
    # open the csv file
    infile = open(fileName)
    reader = csv.reader(infile)
    # loop through each row in reader
    for row in reader:
        # assign variable key to be a string 'lastname, firstname'
        key = row[0] + ", " + row[1]
        # create an empty list to put phone numbers and email addresses in
        user_data = []
        # loop through remaining items in row and append each to the user_data list
        for data in row[2:len(row)]:
            user_data.append(data)
        # create a key-value pair in addressBook using variables key and user_data
        addressBook[key] = user_data
    # close the file
    infile.close()
    return addressBook


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
    # If entry does not exist in address book, print error message
    if (entry not in addrBook.keys()):
        print "Invalid Entry: %s" % entry
    else:
        # If field to edit is 'name', create new key for entry, point new key to prior value, and delete old key
        if field == 'name':
            addrBook[newValue] = addrBook[entry]
            del addrBook[entry]
        # If field to edit is 'phoneNumber', edit the appropriate entry's value (list[0])
        elif field == 'phoneNumber':
            addrBook[entry][0] = newValue
        # If field to edit is 'emailAddress', add new email address to appropriate entry's list
        elif field == 'emailAddress':
            addrBook[entry].append(newValue)
        # If entry is not one of the accepted fields, print error message
        else:
            print "Unexpected field: %s" % field


# Test Cases
JessieAddresses = buildAddrBook('rawAddresses.csv')
print "ADDRESS BOOK IS BUILT! JessieAddresses = ", JessieAddresses

changeEntry(JessieAddresses, 'Lemon, Liz', 'name', 'Lemon, Elizabeth')
print "changeEntry(JessieAddresses, 'Lemon, Liz', 'name', 'Lemon, Elizabeth')."
print "'Lemon, Elizabeth' in JessieAddresses.keys()? Expect True:", 'Lemon, Elizabeth' in JessieAddresses.keys()
print "'Lemon, Liz' in JessieAddresses.keys()? Expect False:", 'Lemon, Liz' in JessieAddresses.keys()

print "changeEntry(JessieAddresses, 'Curry, Steph', 'name', 'Curry, Stephen'). Check: Invalid entry for Curry, Steph =", 
changeEntry(JessieAddresses, 'Curry, Steph', 'name', 'Curry, Stephen')

print "changeEntry(JessieAddresses, 'Potter, Harry', 'friend', 'Weasley, Ron'). Check: Unexpected field: friend =",
changeEntry(JessieAddresses, 'Potter, Harry', 'friend', 'Weasley, Ron')


