def check_valid_move(move):
	# Checks if move contains digits
	try:
		int(move)
		print str(move) + " is not a valid object selection"
		return False
	except ValueError:
		# Checks if move is "rock", "paper", or "scissors"
		if move.lower() == "rock" or move.lower() == "paper" or move.lower() == "scissors":
			return True
		else:
			print move + " is not a valid object selection"
			return False

# Function to determine winner
def determine_winner(p1_move, p2_move):
	# If the players' moves match, there is a tie
	if p1_move == p2_move:
		winner = "We have a tie!"
		return winner
	# If player 1 wins, print "Player 1 wins!"
	elif (p1_move == "rock" and p2_move == "scissors") or\
	(p1_move == "paper" and p2_move == "rock") or\
	(p1_move == "scissors" and p2_move == "paper"):
		winner = "Player 1 wins!"
		return winner
	# If player 1 doesn't win and it isn't a tie, print "Player 2 wins!"
	else:
		winner = "Player 2 wins!"
		return winner

# Rock Paper Scissors Function, takes two strings as arguments
def rps(p1_move, p2_move):
	if not check_valid_move(p1_move):
		return
	if not check_valid_move(p2_move):
		return
	determine_winner(p1_move, p2_move)

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

import unittest

class TestRPS(unittest.TestCase):
	def test_ValidMove(self):
		self.assertTrue(check_valid_move("rock"))
		self.assertFalse(check_valid_move("rock123"))
		self.assertTrue(check_valid_move("SCISSORS"))

	def test_DetermineWinner(self):
		self.assertEqual(determine_winner("rock","paper"), "Player 2 wins!")
		self.assertEqual(determine_winner("scissors","scissors"), "We have a tie!")
		self.assertEqual(determine_winner("scissors","paper"), "Player 1 wins!")
		self.assertIs(determine_winner("rock","paper"), determine_winner("scissors","rock"))

	def test_rps(self):
		self.assertIsNone(rps("rock","paper"))

def multadd(a, b, c):
	return a*b+c

## Test Cases for Exercise 3.2

class TestMultadd(unittest.TestCase):
	def test_multadd(self):
		self.assertEqual(multadd(1, 3, 2), 5)

if __name__ == '__main__':
    unittest.main()
		
