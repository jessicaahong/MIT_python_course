def less_than_6(some_list):
	counter = 0
	for val in some_list:
		if val >= 6:
			counter += 1
	if counter == 0:
		return True
	else:
		return False

# Test Cases
print "Should return False. less_than_6([5,7,3,5]):", less_than_6([5,7,3,5])
print "Should return True. less_than_6([1,5,3,4]):", less_than_6([1,5,3,4])