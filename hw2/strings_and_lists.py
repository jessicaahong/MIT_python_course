"""Thurs May 12 2016"""

# **********  Exercise 4.1 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers

    total = 0
    output = []
    for num in number_list:
        total += num
        output.append(total)
    return output


# Test Cases
print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [100, 10, 1] is:", cumulative_sum([100, 10, 1])
print "cumulative_sum of [50, 60, 70] is:", cumulative_sum([50, 60, 70])
print "cumulative_sum of [-50, 60.5, 70] is:", cumulative_sum([-50, 60.5, 70])

# **********  Exercise 4.2 **********

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    if word[0].lower() in VOWELS:
        return word + "hay"
    else:
        return word[1:] + word[0].lower() + "ay"

# Test Cases
print "pig_latin('alabama') returns:", pig_latin('alabama') 
print "pig_latin('jamboree') returns:", pig_latin('jamboree')
print "pig_latin('Nicholas') returns:", pig_latin('Nicholas')
print "pig_latin('HELLO') returns:", pig_latin('HELLO')

