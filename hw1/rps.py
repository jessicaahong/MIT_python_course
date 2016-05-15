"""Tue May 10 2016"""

def check_valid_move(move):
	# If the user input is rock, paper, or scissors, return True
	if move == "rock" or move == "paper" or move == "scissors":
		return True
	# If not, print error message and return False
	else:
		print "This is not a valid object selection"
		return False

def determine_winner(p1_move, p2_move):
	# If the players' moves match, there is a tie
	if p1_move == p2_move:
		print "We have a tie!"
	# If player 1 wins, print "Player 1 wins!"
	elif (p1_move == "rock" and p2_move == "scissors") or\
	(p1_move == "paper" and p2_move == "rock") or\
	(p1_move == "scissors" and p2_move == "paper"):
		print "Player 1 wins!"
	# If player 1 doesn't win and it isn't a tie, print "Player 2 wins!"
	else:
		print "Player 2 wins!"

def rps():
	# Ask player 1 for move, sanitize input by calling string.lower()
	p1_move = raw_input("Player 1 picks a move! Do you choose rock, paper, or scissors? ").lower()
	# If player 1's move is not valid, this will hit return statement. Game will end.
	if not check_valid_move(p1_move):
		return
	p2_move = raw_input("Player 2 picks a move! Do you choose rock, paper, or scissors? " ).lower()
	if not check_valid_move(p2_move):
		return
	# If both player moves are vaild, run logic to determine winner
	determine_winner(p1_move, p2_move)

rps()