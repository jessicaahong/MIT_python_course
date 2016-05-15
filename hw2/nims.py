"""Wed May 11 2016"""
import unittest

def play_nims(pile, max_stones):
	'''
	An interactive two-person game; also known as Stones.
	@param pile: the number of stones in the pile to start
	@param max_stones: the maximum number of stones you can take on one turn
	'''
	# Only begin game if function arguments are positive integers
	if type(pile) != int or type(max_stones) != int or pile <= 0 or max_stones <= 0:
		error = "Arguments must be positive integers"
		return error

	# Assign current player to be Player 1
	current_player = 1
	print "There are %s stones in the pile" % pile

	while pile > 0:
		valid_move = False
		# Ask player's move
		while valid_move == False:
			stones_removed = raw_input("Player %s's move! Pick a number from 1 to %s: " % (current_player, max_stones))
			try:
				stones_removed_int = int(stones_removed)
			except ValueError:
				print "That is an invalid selection. Must pick a number from 1 to %s, and choice must be smaller than pile: " % (max_stones)
			else:
				if ((1 <= stones_removed_int) and (stones_removed_int <= max_stones) and ((pile - stones_removed_int) >= 0)):
					valid_move = True
				else:
					print "That is an invalid selection. Must pick a number from 1 to %s, and choice must be smaller than pile." % max_stones
		# Execute player's move if move is valid
		pile -= stones_removed_int
		# If pile is now zero, game is won. Print message, terminate game.
		if pile == 0:
			print "Player %s wins!" % current_player
			return "Game Over"
		# Else, print informational message, continue game
		else:
			print "There are now %s stones left." % pile
		# Switch players when pile is still greater than 0
		if current_player == 1:
			current_player = 2
		else:
			current_player = 1

class TestNims(unittest.TestCase):
	def testNims(self):
		self.assertEqual(play_nims(-4,10), "Arguments must be positive integers")
		self.assertEqual(play_nims("banana",10), "Arguments must be positive integers")
		self.assertEqual(play_nims(100,5), "Game Over")

if __name__ == '__main__':
	unittest.main()

