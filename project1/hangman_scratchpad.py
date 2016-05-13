def all_less_than_6(some_list):
	# argument some_list is a list containing integers or floats
	output = True
	for val in some_list:
		if val >= 6:
			output = False
	return output

# Test Cases
print "Should return False. all_less_than_6([5,7,3,5]):", all_less_than_6([5,7,3,5])
print "Should return True. all_less_than_6([1,5,3,4]):", all_less_than_6([1,5,3,4])
print "Should return True. all_less_than_6([1,-5.4,3,4]):", all_less_than_6([1,-5.4,3,4])

def one_less_than_6(some_list):
	# argument some_list is a list containing integers or floats
	output = False
	for val in some_list:
		if val < 6:
			output = True
	return output

print "Should return True. one_less_than_6([5,7,3,5]):", one_less_than_6([5,7,3,5])
print "Should return False. one_less_than_6([7,9,31,14]):", one_less_than_6([7,9,31,14])
print "Should return True. one_less_than_6([9,-5.4,10,101.2]):", one_less_than_6([9,-5.4,10,101.2])