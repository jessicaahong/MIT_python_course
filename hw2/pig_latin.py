import unittest

def piggify_sentence():
	active = True
	while active:
		# Prompt user for sentence to translate to pig latin
		phrase = raw_input("Let's get piggy with it!\nPlease enter a full sentence with only words and spaces. ")
		# If user enters "QUIT", they may exit the while loop and exit the function
		if phrase == "QUIT":
			active = False
		# Else if user does not enter "QUIT"
		else:
			# Create a list of words from the sentence, all in lowercase
			lowercase_word_list = phrase.lower().split()
			# Create a list to store the newly translated words
			output_word_list = []
			for word in lowercase_word_list:
				# Translate word using piggify_word()
				transformed_word = piggify_word(word)
				# Append translated word to output_word_list
				output_word_list.append(transformed_word)
			# Transform word list to string with spaces
			output = ' '.join(output_word_list)
			print output
			# After user uses translator once, display exit message
			print "Exit anytime by typing QUIT"
	return


def piggify_word(word):
	# Argument word is a string to convert to pig-latin
	VOWELS = ["a", "e", "i", "o", "u"]
	special_cases = ["th", "st", "qu", "pl", "tr", "sh"]
	# If word begins with a vowel, concatenate 'hay' at end of word
	if word[0].lower() in VOWELS:
		return word + "hay"
	# If word begins with a special combination of letters (held in list special_cases)
	elif word[0:2].lower() in special_cases:
		# Concatenate first two characters of word, remainder of the word, and "ay"
		return word[2:] + word[0:2].lower() + "ay"
	# If word begins with a consonant and first two letters do not constitute a special case
	else:
		# Concatenate first letter of word with remaining letters of word and "ay"
		return word[1:] + word[0].lower() + "ay"

piggify_sentence()


# TESTING

class TestPigLatin(unittest.TestCase):
	def test_piggify_word(self):
		self.assertEqual(piggify_word("banana"), "ananabay")
		self.assertEqual(piggify_word("eloise"), "eloisehay")
		self.assertEqual(piggify_word("fantastic"), "antasticfay")
		self.assertEqual(piggify_word("things"), "ingsthay")

if __name__ == '__main__':
	unittest.main()