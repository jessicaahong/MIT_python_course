def piggify_sentence():
	active = True
	while active:
		phrase = raw_input("Let's get piggy with it!\n\
			Please enter a full sentence with only words and spaces. ")
		if phrase == "QUIT":
			active = False
		else:
			lowercase_word_list = phrase.lower().split()
			output_word_list = []
			for word in lowercase_word_list:
				transformed_word = piggify_word(word)
				output_word_list.append(transformed_word)
			output = ' '.join(output_word_list)
			print output
			print "Exit anytime by typing QUIT"
	return


def piggify_word(word):
	# word is a string to convert to pig-latin
	VOWELS = ["a", "e", "i", "o", "u"]
	special_cases = ["th", "st", "qu", "pl", "tr", "sh"]
	if word[0].lower() in VOWELS:
		return word + "hay"
	elif word[0:2].lower() in special_cases:
		return word[2:] + word[0:2].lower() + "ay"
	else:
		return word[1:] + word[0].lower() + "ay"

piggify_sentence()

# TESTING
import unittest

class TestPigLatin(unittest.TestCase):
	def test_piggify_word(self):
		self.assertEqual(piggify_word("banana"), "ananabay")
		self.assertEqual(piggify_word("eloise"), "eloisehay")
		self.assertEqual(piggify_word("fantastic"), "antasticfay")
		self.assertEqual(piggify_word("things"), "ingsthay")

if __name__ == '__main__':
	unittest.main()