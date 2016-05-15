def cipher():
	phrase = raw_input("Please enter a phrase to encrypt: ")
	shift = input("Please enter a shift value: ")

	encoded_phrase = ''
	# if shift is not an integer
	if type(shift) != int:
		print "Input error: Shift value must be an integer"
		return
	else:
		# if shift value is < 0
		if shift < 0:
			# transform the shift into a positive integer between 1 and 26
			shift = (-(abs(shift) % 26)) + 26
		for char in phrase:
			# if the character is a letter
			if char.isalpha():
				# if the character is an uppercase letter
				if char.isupper():
					# add shift value to ascii code to create new_code
					new_code = ord(char) + shift
					# if the new_code ascii code > 90 ('Z')
					if new_code > 90:
						# use subtraction and modulus operator to return value between 1 and 26
						to_add = (new_code - 90) % 26
						# add this new value to 64 (the value of 'A' - 1)
						new_code = 64 + to_add
					# push encrypted character to encoded_phrase
					encoded_phrase = encoded_phrase + chr(new_code)
				# else if the character is a lowercase letter...
				else:
					# add shift value to ascii code to create new_code
					new_code = ord(char) + shift
					# if the new_code ascii code > '122' ('z')
					if new_code > 122:
						# use subtraction and modulus operator to return value between 1 and 26
						to_add = (new_code - 122) % 26
						# add this new value to 96 (the value of 'a' -1)
						new_code = 96 + to_add
					# push encrypted charater to encoded_phrase
					encoded_phrase = encoded_phrase + chr(new_code)
			# else if the character is not a letter, just push it to encoded_phrase as is
			else:
				encoded_phrase = encoded_phrase + char

	print "The encoded phrase is:", encoded_phrase

cipher()
