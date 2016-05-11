"""Wed May 11 2016"""

import unittest
import math
import random

##### Template for Homework 2, exercises 3.1-3.4  ######

# **********  Exercise 3.1 ********** 
# Define your rock paper scissors function here

# Function to check if move is valid. If not, prints "This is not a valid object selection"
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
		return
	else:
		# If p1_move and p2_move are both valid, determine winner
		return determine_winner(p1_move, p2_move)

# Test Cases for Exercise 3.1

class TestRPS(unittest.TestCase):
	def test_ValidMove(self):
		self.assertTrue(check_valid_move("rock"))
		self.assertFalse(check_valid_move("rock123"))
		self.assertTrue(check_valid_move("SCISSORS"))
		self.assertFalse(check_valid_move("banana"))

	def test_DetermineWinner(self):
		self.assertEqual(determine_winner("rock","paper"), "Player 2 wins!")
		self.assertEqual(determine_winner("scissors","scissors"), "We have a tie!")
		self.assertEqual(determine_winner("scissors","paper"), "Player 1 wins!")
		self.assertIs(determine_winner("rock","paper"), determine_winner("scissors","rock"))

	def test_RPS(self):
		self.assertIsNotNone(rps("rock","paper"))
		self.assertEqual(rps("rock","rock"), "We have a tie!")
		self.assertEqual(rps("paper","scissors"), "Player 2 wins!")
		self.assertIsNone(rps("banana","rock"))

# *********** Exercise 3.2 ***********
## 1 - multadd function

def multadd(a, b, c):
	return a*b+c

## 2 - Equations

angle_test = multadd(0.5, math.cos(math.pi/4), math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(2, math.log(12, 7), math.ceil(276/float(19)))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(num):
	answer = multadd(num, math.exp(-num), math.sqrt(1-(math.pow(math.e, (-num)))))
	return answer

# Sample Test Cases
x = 5
print "yikes(5) =", yikes(x)

# Test Cases for Exercise 3.2
class TestMathModule(unittest.TestCase):
	def test_Multadd(self):
		self.assertEqual(multadd(9, 5, 4), 49)
		self.assertEqual(multadd(3, 60, 4), 184)
		self.assertEqual(multadd(9, -2, 1), -17)
		self.assertEqual(multadd(-1.5, 2, 3.5), 0.5)

	def test_Equations(self):
		self.assertEqual(angle_test, 1.0606601717798212)
		self.assertEqual(ceiling_test, 17.55397881653925)

	def test_Yikes(self):
		self.assertEqual(yikes(5), 1.0303150673048738)

# ********** Exercise 3.3 **********

## 1 - rand_divis_3 function
def rand_divis_3():
	random_number = random.randint(0, 100)
	print random_number
	if random_number % 3 == 0:
		return True
	else:
		return False

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(num_sides, num_dice):
	if type(num_sides) == int and type(num_dice) == int and num_sides > 0 and num_dice > 0:
		for die in range(num_dice):
			print random.randint(1, num_sides)
		return "That's all!"
	else:
		return "Arguments must be positive integers"
                       

# Test Cases for Exercise 3.3
class TestRandomModule(unittest.TestCase):
	def test_RandDivis3(self):
		self.assertIsNotNone(rand_divis_3())

	def test_RollDice(self):
		self.assertEqual(roll_dice(1,1), "That's all!")
		self.assertEqual(roll_dice('banana', 5), "Arguments must be positive integers")
		self.assertEqual(roll_dice(-14,5), "Arguments must be positive integers")

# Run test cases from the command line

# if __name__ == '__main__':
# 	unittest.main()

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestRPS)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestMathModule)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestRandomModule)
alltests = unittest.TestSuite([suite1, suite2, suite3])
unittest.TextTestRunner(verbosity=2).run(alltests)
