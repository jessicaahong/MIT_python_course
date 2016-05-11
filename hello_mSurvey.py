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
	# Check if p1_move and p2_moves are valid. If either is invalid, exit function.
	if not check_valid_move(p1_move) or not check_valid_move(p2_move):
		return "messed up"
	else:
		# If p1_move and p2_move are both valid, determine winner
		determine_winner(p1_move, p2_move)
