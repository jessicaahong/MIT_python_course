def cipher():
	phrase = raw_input("Please enter a phrase to encrypt: ")
	shift = input("Please enter a shift value: ")

	encoded_phrase = ''

	for char in phrase:
		if char.isalpha():
			if char.isupper():
				encoded_phrase = encoded_phrase + X
			else:
				encoded_phrase = encoded_phrase + X
		else:
			encoded_phrase = encoded_phrase + char

	print "The encoded phrase is:", encoded_phrase

cipher()